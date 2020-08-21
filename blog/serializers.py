from rest_framework import serializers
from django.contrib.auth.models import User
from . models import Post , Category


class UserSerializer1(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class PostSerializer1(serializers.ModelSerializer):
    owner = UserSerializer1(many=False, read_only=True)
    class Meta:
        model = Post
        fields = ['title', 'body', 'owner']

class PostSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'body','created_at']

class CategorySerializer(serializers.ModelSerializer):
    posts = PostSerializer1(many=True, read_only=True, source='post_set')
    url = serializers.HyperlinkedIdentityField(
        view_name="category-detail", read_only=True)
    class Meta:
        model = Category
        fields = ['title',  'created_at', 'posts','url']

class PostSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    owner=UserSerializer1(many=False, read_only=True )
    # category = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name="single-category")
    # category= serializers.StringRelatedField(many=False)
    # category = serializers.SlugRelatedField(many=False, read_only=True, slug_field='title')
    url = serializers.HyperlinkedIdentityField(view_name="post-detail", read_only=True)
    class Meta:
        model = Post
        fields = ['owner', 'title', 'body', 'category','url']

class UserSerializer(serializers.ModelSerializer):
    # posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
    posts=PostSerializer2(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'posts']
