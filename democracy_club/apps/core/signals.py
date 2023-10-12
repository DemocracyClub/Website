from core.cloudfront import invalidate_paths
from django.db.models.signals import post_save
from django.dispatch import receiver
from hermes.models import Post


@receiver(post_save, sender=Post)
def blog_url_invalidation_handler(sender, **kwargs):
    instance = kwargs["instance"]
    path = instance.get_absolute_url()
    invalidate_paths([path, "/blog/", "/", "/research/case_studies/"])
