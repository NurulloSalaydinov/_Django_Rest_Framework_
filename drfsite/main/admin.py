from django.contrib import admin
from .models import User, Category, Tag, Post, PostComment, ReplyPostComment

admin.site.register(User)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    search_fields = ("title",)
    prepopulated_fields = {'slug':('title',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    search_fields = ("title",)
    prepopulated_fields = {'slug':('title',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    search_fields = ("title",)
    prepopulated_fields = {'slug':('title',)}

@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = ("id", "message")
    search_fields = ("message",)


@admin.register(ReplyPostComment)
class ReplyPostCommentAdmin(admin.ModelAdmin):
    list_display = ("id", "message")
    search_fields = ("message",)

