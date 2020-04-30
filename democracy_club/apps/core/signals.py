from django.db.models.signals import post_save
from django.dispatch import receiver

from hermes.models import Post

from core.cloudfront import invalidate_paths


@receiver(post_save, sender=Post)
def blog_url_invalidation_handler(sender, **kwargs):
    instance = kwargs["instance"]
    path = instance.get_absolute_url()
    invalidate_paths([path, "/blog/", "/"])
