from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import (
    Post,
    Category,
    PostComment,
    Tag,
)
from .serializers import (
    PostSerializer, 
    CategorySerializer, 
    PostCommentSerializer,
    TagSerializer,
    PostCommentUpdateSerializer,
)
from .rest_paginations import StandardResultsSetPagination
from rest_framework import permissions
from rest_framework import viewsets



# Post List Api View
class PostAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = StandardResultsSetPagination


# Post Add Api View
class PostAddApiView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def post(self, request, *args, **kwargs):
        author = request.POST.get('author')
        request.POST._mutable = True
        request.POST['post_likes'] = 0
        request.POST['post_bugs'] = 0
        request.POST['post_views'] = 0
        request.POST._mutable = False
        if int(author) == request.user.id:
            return self.create(request, *args, **kwargs)
        else:
            return Response({"hack error": "You can't cheat me"})
        return Response({"status": 200})


# Post Update Api View
class PostUpdateApiView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# Post Delete Api View
class PostDeleteApiView(APIView):
    def delete(self, request, pk):
        try:
            obj = Post.objects.get(id=pk)
        except:
            return Response({"error": "method delete is not allowed"})
        if obj.author == request.user:
            obj.delete()
        else:
            return Response({"error": "You are not author of this post"})
        return Response({'status': 200})


# Post Detail
class PostDetailApiView(APIView):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        return Response({"detail": PostSerializer(post).data})


# CategoryListApiView
class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# TagListApiView
class TagListApiView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


# PostCommentAddApiView
class PostCommentAddApiView(generics.CreateAPIView):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer

    def post(self, request, *args, **kwargs):
        writer = request.POST.get('writer')
        post = request.POST.get('post')
        msg = request.POST.get('message')
        if writer and post and msg:
            if int(writer) == request.user.id:
                obj = Post.objects.get(id=int(post))
                obj.post_comment_count += 1
                obj.save()
                return self.create(request, *args, **kwargs)
            else:
                return Response({"hack error": "you can't cheat me"})
        else:
            return Response({"error": "you must fill all field"})


# PostCommentUpdateView
class PostCommentUpdateView(generics.UpdateAPIView):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentUpdateSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


# post comment delete view
class PostCommentDeleteView(APIView):
    def delete(self, request, pk):
        try:
            obj = PostComment.objects.get(id=pk)
        except:
            return Response({"error": "method delete is not allowed"})
        if obj.writer == request.user:
            obj.delete()
        else:
            return Response({"error": "You are not author of this post"})
        return Response({'status': 200})


