from django.db import models
from django.urls import reverse_lazy
from django_editorjs_fields import EditorJsJSONField, EditorJsTextField
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(
        "Image", upload_to="user-images/%Y/%m/%d", null=True, blank=True)
    username = models.CharField(
        "Username", max_length=256, unique=True, null=True)
    admiring = models.ManyToManyField(
        'User', blank=True, related_name="who_admiring")
    admirer = models.ManyToManyField(
        'User', blank=True, related_name="who_admirer")
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    updated_at = models.DateTimeField("Updated_at", auto_now=True)

    def __str__(self):
        return str(self.username)


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)
    icon = models.ImageField(upload_to='category_icons/%y/%m/%d/')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return str(self.title)


class Tag(models.Model):
    title = models.CharField(max_length=255, unique=True)
    icon = models.ImageField(upload_to='category_icons/%y/%m/%d/')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return str(self.title)


class Post(models.Model):
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    tag = models.ManyToManyField('Tag', blank=True)
    title = models.CharField('Title', max_length=255)
    slug = models.SlugField('*', unique=True)
    body = EditorJsJSONField(
        plugins=[
            '@editorjs/paragraph',
            '@editorjs/image',
            '@editorjs/header',
            '@editorjs/list',
            '@editorjs/quote',
            '@editorjs/inline-code',
            '@editorjs/delimiter',
            '@editorjs/warning',
            '@editorjs/marker',
            '@editorjs/table',
            "editorjs-github-gist-plugin",
            "@editorjs/underline",
            "editorjs-alert@latest",
            # "@bomdi/codebox",
            "editorjs-hyperlink",
            "@calumk/editorjs-codeflask",
        ],
        tools={
            "editorjsCodeflask": {"class": "editorjsCodeflask"},
            "Hyperlink": {
                "class": "Hyperlink",
                "config": {
                    "shortcut": 'CMD+L',
                    "target": '_blank',
                    "rel": 'nofollow',
                    "availableTargets": ['_blank', '_self'],
                    "availableRels": ['author', 'noreferrer'],
                    "validate": False,
                },
                'inlineToolbar': True,
            },
            # "CodeBox": {
            #     "class": "CodeBox",
            #     'inlineToolbar': True,
            #     "config": {
            #         "themeURL": 'https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@9.18.1/build/styles/dracula.min.css',  # Optional
            #         "themeName": 'atom-one-dark',  # Optional
            #         # Optional. This also determines the background color of the language select drop-down
            #         "useDefaultTheme": 'light'
            #     }
            # },
            "Gist": {
                "class": "Gist"  # Include the plugin class. See docs Editor.js plugins
            },
            'Image': {
                'class': 'ImageTool',
                'inlineToolbar': True,
                "config": {
                    "endpoints": {
                        "byFile": reverse_lazy('editorjs_image_upload'),
                        "byUrl": reverse_lazy('editorjs_image_by_url')
                    }
                },
            },
            'Header': {
                'class': 'Header',
                'inlineToolbar': True,
                'config': {
                    'placeholder': 'Enter a header',
                    'levels': [1, 2, 3, 4],
                    'defaultLevel': 2,
                }
            },
            'List': {'class': 'List', 'inlineToolbar': True},
            'Quote': {'class': 'Quote', 'inlineToolbar': True},
            'InlineCode': {'class': 'InlineCode'},
            'Delimiter': {'class': 'Delimiter'},
            'Warning': {'class': 'Warning', 'inlineToolbar': True},
            'Marker': {'class': 'Marker', 'inlineToolbar': True},
            'Table': {'class': 'Table', 'inlineToolbar': True},
            'Underline': {'class': 'Underline'},
            'Alert': {'class': 'Alert', 'inlineToolbar': True},
        },
        i18n={
            'messages': {
                'blockTunes': {
                    "delete": {
                        "Delete": "Удалить"
                    },
                    "moveUp": {
                        "Move up": "Переместить вверх"
                    },
                    "moveDown": {
                        "Move down": "Переместить вниз"
                    }
                }
            },
        },
        blank=True,
        null=True,
    )
    post_views = models.IntegerField(default=0)
    post_likes = models.IntegerField(default=0)
    post_bugs = models.IntegerField(default=0)
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    updated_at = models.DateTimeField("Updated at", auto_now=True)

    def __str__(self):
        return str(self.title)


class PostComment(models.Model):
    writer = models.ForeignKey('User', on_delete=models.CASCADE)
    post = models.ForeignKey(
        'Post', on_delete=models.CASCADE, related_name='post_comments')
    message = models.CharField('Message', max_length=255)

    def __str__(self):
        return str(self.message)


class ReplyPostComment(models.Model):
    writer = models.ForeignKey('User', on_delete=models.CASCADE)
    comment = models.ForeignKey(
        'PostComment', on_delete=models.CASCADE, related_name='post_reply_comments')
    message = models.CharField('Message', max_length=255)

    def __str__(self):
        return str(self.message)
