from django.db import migrations, models
from django.utils.text import slugify

# Display names for the tags that used to be hard-coded in the admin form.
# Any other values found in the data use the raw value as the name.
TAG_NAMES = {
    "WhoCanIVoteFor": "WhoCanIVoteFor",
    "CaseStudy": "Case Study",
    "Research": "Research",
    "Elections": "Elections",
    "Councils": "Councils",
    "Candidates": "Candidates",
    "Representatives": "Representatives",
    "Data": "Data",
    "WhereDoIVote": "WhereDoIVote",
    "Election_Leaflets": "Election Leaflets",
    "EveryElection": "EveryElection",
    "Ideas": "Ideas",
    "Impact": "Impact",
    "Featured": "Featured",
    "Widget": "Widget",
    "ParishCouncils": "Parish councils",
}


def legacy_slug(value):
    # Lower-cased old value, so existing /blog/tag/<OldValue>/ URLs still
    # resolve (tag lookups are case-insensitive).
    return slugify(value)


def array_to_m2m(apps, schema_editor):
    Post = apps.get_model("hermes", "Post")
    Tag = apps.get_model("hermes", "Tag")

    tags_by_slug = {}

    def get_tag(value):
        slug = legacy_slug(value)
        if slug not in tags_by_slug:
            tags_by_slug[slug], _ = Tag.objects.get_or_create(
                slug=slug, defaults={"name": TAG_NAMES.get(value, value)}
            )
        return tags_by_slug[slug]

    # Create all the previously-available tags, even if unused
    for value in TAG_NAMES:
        get_tag(value)

    for post in Post.objects.exclude(tags=[]):
        post.new_tags.set([get_tag(value) for value in post.tags])


def m2m_to_array(apps, schema_editor):
    Post = apps.get_model("hermes", "Post")
    slug_to_value = {legacy_slug(value): value for value in TAG_NAMES}
    for post in Post.objects.prefetch_related("new_tags"):
        post.tags = [
            slug_to_value.get(tag.slug, tag.name)[:30]
            for tag in post.new_tags.all()
        ]
        post.save(update_fields=["tags"])


class Migration(migrations.Migration):
    dependencies = [
        ("hermes", "0013_alter_post_hero_alt_text"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="The name shown on the site, e.g. 'Case Study'",
                        max_length=100,
                        unique=True,
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        help_text="Used in URLs, e.g. /blog/tag/case-study/",
                        max_length=100,
                        unique=True,
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
            },
        ),
        migrations.AddField(
            model_name="post",
            name="new_tags",
            field=models.ManyToManyField(
                blank=True, related_name="+", to="hermes.tag"
            ),
        ),
        migrations.RunPython(array_to_m2m, m2m_to_array),
        migrations.RemoveField(
            model_name="post",
            name="tags",
        ),
        migrations.RenameField(
            model_name="post",
            old_name="new_tags",
            new_name="tags",
        ),
        migrations.AlterField(
            model_name="post",
            name="tags",
            field=models.ManyToManyField(
                blank=True, related_name="posts", to="hermes.tag"
            ),
        ),
    ]
