# Generated by Django 4.2.6 on 2023-10-18 12:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hermes", "0011_alter_post_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="hero_alt_text",
            field=models.CharField(
                blank=True,
                max_length=100,
                null=True,
                verbose_name="hero alt text",
            ),
        ),
    ]
