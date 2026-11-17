from django.db import migrations
from django.utils.text import slugify

# Tag values (and their display names) from before tags were a model.
# URLs like /blog/tag/CaseStudy/ have been published and linked to, so make
# sure they keep working even if the tag's slug has since been changed.
LEGACY_TAGS = {
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


def add_legacy_redirects(apps, schema_editor):
    Tag = apps.get_model("hermes", "Tag")
    TagSlugRedirect = apps.get_model("hermes", "TagSlugRedirect")

    for value, name in LEGACY_TAGS.items():
        legacy_slug = slugify(value)
        if Tag.objects.filter(slug__iexact=legacy_slug).exists():
            continue  # Still the tag's slug, nothing to do
        if TagSlugRedirect.objects.filter(
            old_slug__iexact=legacy_slug
        ).exists():
            continue
        tag = Tag.objects.filter(name=name).first()
        if tag:
            TagSlugRedirect.objects.create(old_slug=legacy_slug, tag=tag)


class Migration(migrations.Migration):
    dependencies = [
        ("hermes", "0015_tag_slug_redirect"),
    ]

    operations = [
        migrations.RunPython(add_legacy_redirects, migrations.RunPython.noop),
    ]
