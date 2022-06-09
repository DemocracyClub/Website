from django.contrib import admin

from hermes.models import Post, Category


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("subject",),
    }


class CategoryAdmin(admin.ModelAdmin):
    include = (
        "title",
        "parent",
    )
    exclude = ("slug",)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
