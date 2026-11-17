from django.contrib import admin
from django.db.models import Count
from hermes.models import Category, Post, Tag, TagSlugRedirect


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("subject",),
    }
    filter_horizontal = ["author", "tags"]
    search_fields = ["subject"]
    search_help_text = "Search by subject (Post title)"
    list_display = ["subject", "created_on", "category", "tag_list"]
    list_filter = ["is_published", "tags", "author"]

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("tags")

    @admin.display(description="Tags")
    def tag_list(self, obj):
        return ", ".join(tag.name for tag in obj.tags.all())


class TagSlugRedirectInline(admin.TabularInline):
    model = TagSlugRedirect
    extra = 0
    verbose_name = "old slug"
    verbose_name_plural = (
        "Old slugs (these URLs redirect to this tag, and are added "
        "automatically when you change the slug)"
    )


class TagAdmin(admin.ModelAdmin):
    inlines = [TagSlugRedirectInline]
    list_display = ["name", "slug", "post_count"]
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ["name", "slug"]

    def get_queryset(self, request):
        return (
            super()
            .get_queryset(request)
            .annotate(post_count=Count("posts", distinct=True))
        )

    @admin.display(description="Posts", ordering="post_count")
    def post_count(self, obj):
        return obj.post_count


class CategoryAdmin(admin.ModelAdmin):
    include = (
        "title",
        "parent",
    )
    exclude = ("slug",)


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
