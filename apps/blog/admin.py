from django.contrib import admin

from apps.blog.models import Blog, Category, Comments


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "enabled")


admin.site.register(Category)


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ("text", "blog")
