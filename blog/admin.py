from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "content",
        "created_at",
        "is_active_publication",
        "views_counter",
    )
    search_fields = (
        "title",
        "content",
    )
