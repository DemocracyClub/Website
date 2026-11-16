import operator
import os
from functools import reduce

from django.conf import settings as django_settings
from django.core.exceptions import ValidationError
from django.db import models, transaction
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.urls import reverse
from django.utils.text import Truncator, slugify
from django.utils.translation import gettext as _

from . import settings


class TimestampedModel(models.Model):
    created_on = models.DateTimeField(_("created on"), auto_now_add=True)
    modified_on = models.DateTimeField(_("modified on"), auto_now=True)

    class Meta:
        abstract = True


class CategoryManager(models.Manager):
    def children_of(self, category, categories=None):
        if categories is None:
            categories = list(self.all())

        children = list(filter(lambda c: c.parent == category, categories))
        for child in children:
            children.extend(self.children_of(child, categories))

        return children


class Category(models.Model):
    title = models.CharField(_("title"), max_length=100)
    parent = models.ForeignKey(
        "self", blank=True, null=True, on_delete=models.CASCADE
    )
    slug = models.CharField(
        blank=True, default="", max_length=500, db_index=True
    )

    objects = CategoryManager()

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def save(self, *args, **kwargs):
        self.slug = self._generate_slug()
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return " > ".join([category.title for category in self.hierarchy()])

    def __str__(self):
        return self.__unicode__()

    def get_absolute_url(self):
        return reverse("hermes_category_post_list", kwargs={"slug": self.slug})

    def _generate_slug(self):
        return "/".join(
            [slugify(category.title) for category in self.hierarchy()]
        ).lower()

    @property
    def is_root(self):
        """Returns True if this category has no parent."""
        return self.parent is None

    def parents(self):
        """Returns a list of all the current category's parents."""
        parents = []

        if self.parent is None:
            return []

        category = self
        while category.parent is not None:
            parents.append(category.parent)
            category = category.parent

        return parents[::-1]

    def hierarchy(self):
        return self.parents() + [self]

    def root_parent(self, category=None):
        """Returns the topmost parent of the current category."""
        return next(filter(lambda c: c.is_root, self.hierarchy()))


class TagManager(models.Manager):
    def resolve(self, slug):
        """
        Find a tag by slug, case-insensitively, falling back to slugs the
        tag used to have. Returns None if nothing matches.

        Callers can compare `tag.slug` to the slug they asked for to tell
        whether they should redirect to the canonical URL.
        """
        if not slug:
            return None
        # Slugs are always stored lower case, so these exact lookups can
        # use the unique indexes (unlike __iexact)
        slug = slug.lower()
        tag = self.filter(slug=slug).first()
        if tag:
            return tag
        redirect = (
            TagSlugRedirect.objects.select_related("tag")
            .filter(old_slug=slug)
            .first()
        )
        return redirect.tag if redirect else None

    def matching_slug(self, slug):
        """
        A lazy queryset of the tag with this current or old slug, for use
        in subqueries. Doesn't hit the database until evaluated.
        """
        if not slug:
            return self.none()
        slug = slug.lower()
        return self.filter(
            models.Q(slug=slug) | models.Q(slug_redirects__old_slug=slug)
        )


class Tag(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="The name shown on the site, e.g. 'Case Study'",
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        help_text=(
            "Used in URLs, e.g. /blog/tag/case-study/. If you change this, "
            "the old URL will redirect to the new one."
        ),
    )

    objects = TagManager()

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("hermes_post_list_by_tag", kwargs={"tag": self.slug})

    def clean(self):
        super().clean()
        if self.slug:
            self.slug = self.slug.lower()
            clash = Tag.objects.filter(slug=self.slug).exclude(pk=self.pk)
            if clash.exists():
                raise ValidationError(
                    {"slug": "Another tag already uses this slug."}
                )

    def save(self, *args, **kwargs):
        self.slug = self.slug.lower()
        old_slug = None
        if self.pk:
            old_slug = (
                Tag.objects.filter(pk=self.pk)
                .values_list("slug", flat=True)
                .first()
            )
        with transaction.atomic():
            super().save(*args, **kwargs)
            # This slug now belongs to this tag, so it can't redirect anywhere
            TagSlugRedirect.objects.filter(old_slug=self.slug).delete()
            if old_slug and old_slug != self.slug:
                TagSlugRedirect.objects.update_or_create(
                    old_slug=old_slug, defaults={"tag": self}
                )


class TagSlugRedirect(models.Model):
    """
    A slug a tag used to have. Requests for the old slug redirect to the
    tag's current URL. Created automatically when a tag's slug changes.
    """

    old_slug = models.SlugField(max_length=100, unique=True)
    tag = models.ForeignKey(
        Tag, related_name="slug_redirects", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ("old_slug",)

    def __str__(self):
        return f"{self.old_slug} → {self.tag.slug}"

    def save(self, *args, **kwargs):
        self.old_slug = self.old_slug.lower()
        super().save(*args, **kwargs)


class PostQuerySet(models.query.QuerySet):
    def by(self, author):
        return self.filter(author__username=author)

    def in_category(self, category_slug):
        category = Category.objects.get(slug=category_slug)
        children = Category.objects.children_of(category)

        return self.filter(category__in=[category] + children)

    def created_on(self, year=None, month=None, day=None):
        clauses = []

        if year:
            clauses.append(models.Q(created_on__year=year))

        if month:
            clauses.append(models.Q(created_on__month=month))

        if day:
            clauses.append(models.Q(created_on__day=day))

        return self.filter(reduce(operator.__and__, clauses))

    def recent(self, limit=None):
        queryset = self.published()
        if limit:
            queryset = queryset[:limit]

        return queryset

    def random(self, limit=None):
        queryset = self.recent().order_by("?")
        if limit:
            queryset = queryset[:limit]

        return queryset

    def published(self):
        return self.filter(is_published=True)

    def for_tag(self, tag):
        """
        Filter to posts with the given tag. `tag` can be a Tag instance
        or a tag slug (matched case-insensitively, following old slugs).
        """
        if isinstance(tag, Tag):
            return self.filter(tags=tag)
        return self.filter(tags__in=Tag.objects.matching_slug(tag))


class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def in_category(self, category_slug):
        return self.get_queryset().in_category(category_slug)

    def created_on(self, year=None, month=None, day=None):
        return self.get_queryset().created_on(year=year, month=month, day=day)

    def recent(self, limit=None):
        return self.get_queryset().recent(limit=limit)

    def random(self, limit=None):
        return self.get_queryset().random(limit=limit)

    def published(self):
        return self.get_queryset().published()

    def by(self, author):
        return self.get_queryset().by(author)

    def for_tag(self, tag):
        return self.get_queryset().for_tag(tag)


def post_hero_upload_to(instance, filename):
    filename = os.path.split(filename)[-1]
    filename, extension = os.path.splitext(filename)
    extension = extension[1:]

    return "hermes/heroes/{slug}_{filename}_hero.{extension}".format(
        slug=instance.slug[:40], filename=filename[:30], extension=extension
    )


class Post(TimestampedModel):
    is_published = models.BooleanField(default=False)
    hero = models.ImageField(
        _("hero"), upload_to=post_hero_upload_to, blank=True, null=True
    )
    hero_alt_text = models.CharField(
        _("hero alt text"), max_length=100, blank=True
    )
    subject = models.CharField(_("subject"), max_length=100)
    slug = models.SlugField(_("slug"), max_length=100, unique=True)
    summary = models.TextField(_("summary"), blank=True, null=True)
    body = models.TextField(_("body"))

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ManyToManyField(
        django_settings.AUTH_USER_MODEL, verbose_name="Authors"
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="posts")

    objects = PostManager()

    class Meta:
        ordering = ("-created_on",)
        get_latest_by = "modified_on"

    def __unicode__(self):
        return self.subject

    def __str__(self):
        return self.__unicode__()

    def get_absolute_url(self):
        return reverse(
            "hermes_post_detail",
            kwargs={
                "year": self.created_on.year,
                "month": self.created_on.strftime("%m"),
                "day": self.created_on.strftime("%d"),
                "slug": self.slug,
            },
        )

    @property
    def short(self):
        if self.summary:
            return self.rendered_summary
        return Truncator(self.rendered).words(
            settings.HERMES_SHORT_TRUNCATE_WORDS,
            truncate="…",
            html=True,
        )

    @property
    def rendered_summary(self):
        return self._rendered_attribute("summary")

    @property
    def rendered(self):
        return self._rendered_attribute("body")

    def _rendered_attribute(self, attr_name):
        attr_value = getattr(self, attr_name)
        if settings.MARKUP_RENDERER:
            return settings.MARKUP_RENDERER(attr_value)
        return attr_value

    def _generate_slug(self):
        return slugify(self.subject)

    def save(self, *args, **kwargs):
        self.slug = self._generate_slug()
        super(Post, self).save(*args, **kwargs)

    @property
    def reading_time(self):
        time = (self.summary.count(" ") + self.body.count(" ")) / 300
        if time == 0:
            time = 1
        return time


def postfile_upload_to(instance, filename):
    return "uploads/hermes/{article}/{filename}".format(
        article=instance.pk, filename=filename
    )


class PostFile(models.Model):
    post = models.ForeignKey(
        Post, related_name="files", on_delete=models.CASCADE
    )
    f = models.FileField(upload_to=postfile_upload_to)

    class Meta:
        verbose_name = "PostFile"
        verbose_name_plural = "PostFiles"

    def __unicode__(self):
        return "File for {}".format(self.post)

    def __str__(self):
        return self.__unicode__()


@receiver(pre_delete, sender=PostFile)
def postfile_delete(sender, instance, **kwargs):
    instance.f.delete(False)
