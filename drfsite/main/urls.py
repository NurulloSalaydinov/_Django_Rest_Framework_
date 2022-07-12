from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    PostAPIView, 
    PostAddApiView, 
    PostUpdateApiView, 
    PostDeleteApiView, 
    PostDetailApiView,
    CategoryListAPIView,
    PostCommentAddModelViewSet
)

app_name = 'main'

router = DefaultRouter()
router.register(r'comments', PostCommentAddModelViewSet, basename='post-comments')

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
    # post comments include
    path('post-comments/', include(router.urls))
]
