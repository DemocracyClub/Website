import csv

from django.conf import settings
from django.db import migrations


def get_post_by_slug(Post, slug):
    try:
        return Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        return None


def get_user_by_username(User, username):
    try:
        return User.objects.get(username=username)
    except User.DoesNotExist:
        return None


def get_authors_for_past_posts(apps, schema_editor):
    with open(
        "democracy_club/apps/hermes/blog-authors-2022-06-28.csv"
    ) as csvfile:
        Post = apps.get_model("hermes", "Post")
        User = apps.get_model("auth", "User")
        reader = csv.DictReader(csvfile)
        for row in reader:
            username = row["username"]
            slug = row["slug"]
            blog_post = get_post_by_slug(Post, slug)
            if blog_post:
                author = get_user_by_username(User, username)
                if author:
                    blog_post.author.add(author)
                    blog_post.save()
                else:
                    print("Author not found: " + author)


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("hermes", "0009_alter_post_author"),
    ]

    operations = [
        migrations.RunPython(
            get_authors_for_past_posts, migrations.RunPython.noop
        ),
    ]
