from rest_framework import serializers

from .models import Post, Category, PostComment, Tag, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'avatar', 'username']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class PostCommentSerializer(serializers.ModelSerializer):
    writer = UserSerializer(read_only=True)
    class Meta:
        model = PostComment
        fields = '__all__'


class PostCommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = '__all__'
        read_only_fields = ['writer', 'post']


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    author = UserSerializer(read_only=True)
    tag = TagSerializer(read_only=True, many=True)
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['created_at']


class PostAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['created_at']
