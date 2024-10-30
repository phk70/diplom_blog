from django.contrib import admin

from .models import Post, Comment


admin.site.site_header = "Блог TripMap"
admin.site.site_title = "Админка TripMap"


class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "published_date")
    search_fields = ("title",)
    

class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "author", "text", "created_date")
    search_fields = ("text",)
    sortable_by = ("created_date",)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
