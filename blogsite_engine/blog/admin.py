from django.contrib import admin
from django.contrib.auth.models import Group

from .models import User, Tag, Post, Comment


admin.site.site_header = "Admin dashboard for Django blog"


class PostAdmin(admin.ModelAdmin):
    list_display = ("post_title", "post_publish_time", "author")
    list_filter = ("post_title", "post_publish_time", "author")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("comment_text", "comment_author", "comment_time", 'post')
    list_filter = ("comment_text", "comment_author", "comment_time", 'post')


admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

admin.site.unregister(Group)