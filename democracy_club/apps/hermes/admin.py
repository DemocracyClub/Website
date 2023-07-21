from django.contrib import admin
from hermes.models import Category, Post


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("subject",),
    }
    filter_horizontal = ["author"]
    search_fields = ["subject"]
    search_help_text = "Search by subject (Post title)"
    list_display = ["subject", "created_on", "category"]
    list_filter = ["is_published", "author"]


class CategoryAdmin(admin.ModelAdmin):
    include = (
        "title",
        "parent",
    )
    exclude = ("slug",)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
