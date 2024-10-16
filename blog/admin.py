from django.contrib import admin

from .models import Post


admin.site.site_header = "Блог TravelMap"
admin.site.site_title = "Админка TravelMap"

class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "published_date")
    search_fields = ("title",)

admin.site.register(Post, PostAdmin)