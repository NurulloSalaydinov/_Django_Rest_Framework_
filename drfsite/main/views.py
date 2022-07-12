from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post, Category, PostComment
from .serializers import PostSerializer, CategorySerializer, PostCommentSerializer
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


# PostCommentAddApiView
class PostCommentAddApiView(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        print(request.POST)
        


# class WomenAPIView(APIView):
#     def get(self, request):
#         w = Women.objects.all()
#         return Response({'data': WomenSerializer(w, many=True).data})
    
#     def post(self, request):
#         print(request.data)
#         # return Response({'status': 200})
#         d = request.data
#         title = d.get('title')
#         content = d.get('content')
#         cat_id = d.get('cat_id')
#         if title and content and cat_id:
#             post_new = Women.objects.create(
#                 title = title,
#                 content=content,
#                 cat_id=cat_id,
#             )
#             return Response({'title': title, 'content': content, 'id': post_new.id})
#         else:
#             return Response({'error': 'Try Again'})
#     def delete(self, request):
#         print('delete: Delete', request.data)

#     def put(self, request):
#         print('Put: Update', request.data)


