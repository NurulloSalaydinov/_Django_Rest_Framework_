from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    PostAPIView, 
    PostAddApiView, 
    PostUpdateApiView, 
    PostDeleteApiView, 
    PostDetailApiView,
    CategoryListAPIView,
    TagListApiView,
    PostCommentAddApiView,
    PostCommentUpdateView,
    PostCommentDeleteView
)

app_name = 'main'

urlpatterns = [
    # post path
    path('post-lists/', PostAPIView.as_view(), name='post_lists'),
    path('post-new/', PostAddApiView.as_view(), name='post_add'),
    path('post-update/<int:pk>/', PostUpdateApiView.as_view(), name='post_update'),
    path('post-delete/<int:pk>/', PostDeleteApiView.as_view(), name='post_delete'),
    path('post-detail/<slug:slug>/', PostDetailApiView.as_view(), name='post_detail'),
    # end post path
    # category list
    path('category-lists/', CategoryListAPIView.as_view(), name='category_lists'),
    # tag list
    path('tag-lists/', TagListApiView.as_view(), name='tag_lists'),
    # post comment path
    path('post-comment-new/', PostCommentAddApiView.as_view(), name='post_comment_new'),
    # update
    path('post-comment-update/<int:pk>/', PostCommentUpdateView.as_view(), name='post-comment-update'),
    # delete
    path('post-comment-delete/<int:pk>/', PostCommentDeleteView.as_view(), name='post-comment-delete'),
    # end post comment path
]
