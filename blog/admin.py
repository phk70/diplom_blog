from django.contrib import admin

from .models import Post, Comment


admin.site.site_header = "Блог TravelMap"
admin.site.site_title = "Админка TravelMap"

class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "published_date")
    search_fields = ("title",)

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "author", "text", "created_date")
    search_fields = ("text",)
    sortable_by = ("created_date",)

admin.site.register(Comment, CommentAdmin)