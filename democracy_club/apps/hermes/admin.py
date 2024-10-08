from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from hermes.models import Category, Post


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

    tag_values = [
        ("WhoCanIVoteFor", "WhoCanIVoteFor"),
        ("CaseStudy", "Case Study"),
        ("Research", "Research"),
        ("Elections", "Elections"),
        ("Councils", "Councils"),
        ("Candidates", "Candidates"),
        ("Representatives", "Representatives"),
        ("Data", "Data"),
        ("WhereDoIVote", "WhereDoIVote"),
        ("Election_Leaflets", "Election Leaflets"),
        ("EveryElection", "EveryElection"),
        ("Ideas", "Ideas"),
        ("Impact", "Impact"),
        ("Featured", "Featured"),
        ("Widget", "Widget"),
    ]

    tags = forms.MultipleChoiceField(
        choices=tag_values,
        widget=FilteredSelectMultiple("tags", False),
        required=False,
    )


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

    prepopulated_fields = {
        "slug": ("subject",),
    }
    filter_horizontal = ["author"]
    search_fields = ["subject"]
    search_help_text = "Search by subject (Post title)"
    list_display = ["subject", "created_on", "category", "tags"]
    list_filter = ["is_published", "author"]


class CategoryAdmin(admin.ModelAdmin):
    include = (
        "title",
        "parent",
    )
    exclude = ("slug",)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
