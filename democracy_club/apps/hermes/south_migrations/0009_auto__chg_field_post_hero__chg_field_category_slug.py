# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):
    def forwards(self, orm):

        # Changing field 'Post.hero'
        db.alter_column(
            "hermes_post",
            "hero",
            self.gf("django.db.models.fields.files.ImageField")(
                max_length=100, null=True
            ),
        )

        # Changing field 'Category.slug'
        db.alter_column(
            "hermes_category",
            "slug",
            self.gf("django.db.models.fields.CharField")(max_length="500"),
        )

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Post.hero'
        raise RuntimeError(
            "Cannot reverse this migration. 'Post.hero' and its values cannot be restored."
        )

        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Post.hero'
        db.alter_column(
            "hermes_post",
            "hero",
            self.gf("django.db.models.fields.files.ImageField")(max_length=100),
        )

        # Changing field 'Category.slug'
        db.alter_column(
            "hermes_category",
            "slug",
            self.gf("django.db.models.fields.SlugField")(max_length=50),
        )

    models = {
        "auth.group": {
            "Meta": {"object_name": "Group"},
            "id": (
                "django.db.models.fields.AutoField",
                [],
                {"primary_key": "True"},
            ),
            "name": (
                "django.db.models.fields.CharField",
                [],
                {"unique": "True", "max_length": "80"},
            ),
            "permissions": (
                "django.db.models.fields.related.ManyToManyField",
                [],
                {
                    "to": "orm['auth.Permission']",
                    "symmetrical": "False",
                    "blank": "True",
                },
            ),
        },
        "auth.permission": {
            "Meta": {
                "ordering": "(u'content_type__app_label', u'content_type__model', u'codename')",
                "unique_together": "((u'content_type', u'codename'),)",
                "object_name": "Permission",
            },
            "codename": (
                "django.db.models.fields.CharField",
                [],
                {"max_length": "100"},
            ),
            "content_type": (
                "django.db.models.fields.related.ForeignKey",
                [],
                {"to": "orm['contenttypes.ContentType']"},
            ),
            "id": (
                "django.db.models.fields.AutoField",
                [],
                {"primary_key": "True"},
            ),
            "name": (
                "django.db.models.fields.CharField",
                [],
                {"max_length": "50"},
            ),
        },
        "auth.user": {
            "Meta": {"object_name": "User"},
            "date_joined": (
                "django.db.models.fields.DateTimeField",
                [],
                {"default": "datetime.datetime.now"},
            ),
            "email": (
                "django.db.models.fields.EmailField",
                [],
                {"max_length": "75", "blank": "True"},
            ),
            "first_name": (
                "django.db.models.fields.CharField",
                [],
                {"max_length": "30", "blank": "True"},
            ),
            "groups": (
                "django.db.models.fields.related.ManyToManyField",
                [],
                {
                    "symmetrical": "False",
                    "related_name": "u'user_set'",
                    "blank": "True",
                    "to": "orm['auth.Group']",
                },
            ),
            "id": (
                "django.db.models.fields.AutoField",
                [],
                {"primary_key": "True"},
            ),
            "is_active": (
                "django.db.models.fields.BooleanField",
                [],
                {"default": "True"},
            ),
            "is_staff": (
                "django.db.models.fields.BooleanField",
                [],
                {"default": "False"},
            ),
            "is_superuser": (
                "django.db.models.fields.BooleanField",
                [],
                {"default": "False"},
            ),
            "last_login": (
                "django.db.models.fields.DateTimeField",
                [],
                {"default": "datetime.datetime.now"},
            ),
            "last_name": (
                "django.db.models.fields.CharField",
                [],
                {"max_length": "30", "blank": "True"},
            ),
            "password": (
                "django.db.models.fields.CharField",
                [],
                {"max_length": "128"},
            ),
            "user_permissions": (
                "django.db.models.fields.related.ManyToManyField",
                [],
                {
                    "symmetrical": "False",
                    "related_name": "u'user_set'",
                    "blank": "True",
                    "to": "orm['auth.Permission']",
                },
            ),
            "username": (
                "django.db.models.fields.CharField",
                [],
                {"unique": "True", "max_length": "30"},
            ),
        },
        "contenttypes.contenttype": {
            "Meta": {
                "ordering": "('name',)",
                "unique_together": "(('app_label', 'model'),)",
                "object_name": "ContentType",
                "db_table": "'django_content_type'",
            },
            "app_label": (
                "django.db.models.fields.CharField",
                [],
                {"max_length": "100"},
            ),
            "id": (
                "django.db.models.fields.AutoField",
                [],
                {"primary_key": "True"},
            ),
            "model": (
                "django.db.models.fields.CharField",
                [],
                {"max_length": "100"},
            ),
            "name": (
                "django.db.models.fields.CharField",
                [],
                {"max_length": "100"},
            ),
        },
        "hermes.category": {
            "Meta": {"object_name": "Category"},
            "id": (
                "django.db.models.fields.AutoField",
                [],
                {"primary_key": "True"},
            ),
            "parent": (
                "django.db.models.fields.related.ForeignKey",
                [],
                {
                    "to": "orm['hermes.Category']",
                    "null": "True",
                    "blank": "True",
                },
            ),
            "slug": (
                "django.db.models.fields.CharField",
                [],
                {
                    "default": "''",
                    "max_length": "'500'",
                    "db_index": "True",
                    "blank": "True",
                },
            ),
            "title": (
                "django.db.models.fields.CharField",
                [],
                {"max_length": "100"},
            ),
        },
        "hermes.post": {
            "Meta": {"ordering": "('-created_on',)", "object_name": "Post"},
            "author": (
                "django.db.models.fields.related.ForeignKey",
                [],
                {"to": "orm['auth.User']"},
            ),
            "body": ("django.db.models.fields.TextField", [], {}),
            "category": (
                "django.db.models.fields.related.ForeignKey",
                [],
                {"to": "orm['hermes.Category']"},
            ),
            "created_on": (
                "django.db.models.fields.DateTimeField",
                [],
                {"auto_now_add": "True", "blank": "True"},
            ),
            "hero": (
                "django.db.models.fields.files.ImageField",
                [],
                {"max_length": "100", "null": "True", "blank": "True"},
            ),
            "id": (
                "django.db.models.fields.AutoField",
                [],
                {"primary_key": "True"},
            ),
            "modified_on": (
                "django.db.models.fields.DateTimeField",
                [],
                {"auto_now": "True", "blank": "True"},
            ),
            "slug": (
                "django.db.models.fields.SlugField",
                [],
                {"max_length": "100"},
            ),
            "subject": (
                "django.db.models.fields.CharField",
                [],
                {"max_length": "100"},
            ),
            "summary": (
                "django.db.models.fields.TextField",
                [],
                {"null": "True", "blank": "True"},
            ),
        },
    }

    complete_apps = ["hermes"]
