from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    PostAPIView, 
    PostAddApiView, 
    PostUpdateApiView, 
    PostDeleteApiView, 
    PostDetailApiView,
    CategoryListAPIView,
    PostCommentAddApiView
)

app_name = 'main'

urlpatterns = [
    # post path
    path('post-lists/', PostAPIView.as_view(), name='post_list'),
    path('post-new/', PostAddApiView.as_view(), name='post_add'),
    path('post-update/<int:pk>/', PostUpdateApiView.as_view(), name='post_update'),
    path('post-delete/<int:pk>/', PostDeleteApiView.as_view(), name='post_delete'),
    path('post-detail/<slug:slug>/', PostDetailApiView.as_view(), name='post_detail'),
    # end post path
    # category path
    path('category-list/', CategoryListAPIView.as_view(), name='category-list'),
    # post comment path
    path('post-comment-new', PostCommentAddApiView.as_view(), name='post-comment-new'),
    # end post comment path
]
