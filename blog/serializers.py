from rest_framework import serializers
from django.contrib.auth.models import User
from . models import Post , Category


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'posts']

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['title']


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # category = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name="single-category")
    # category= serializers.StringRelatedField(many=False)
    category= serializers.SlugRelatedField(many=False, read_only=True, slug_field='title')
    class Meta:
        model = Post
        fields = ['owner','title', 'body', 'category']
