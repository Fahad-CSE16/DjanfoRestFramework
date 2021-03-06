from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAdminUser
from rest_framework import permissions, viewsets
from rest_framework import generics
from .models import Post, Category
from .permissions import IsOwnerOrReadOnly, IsOwnerOrIsAdminOrReadOnly
from django.contrib.auth.models import User
from rest_framework.reverse import reverse

from . serializers import PostSerializer, CategorySerializer,UserSerializer


# Create your views here.
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes= [permissions.IsAdminUser]


# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset= Post.objects.all()
    serializer_class = PostSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# class PostList(generics.ListCreateAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     queryset= Post.objects.all()
#     serializer_class = PostSerializer
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)


# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrIsAdminOrReadOnly]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class CategoryList(generics.ListAPIView):
#     # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


class CategoryCreate(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# class CategoryDetail(generics.RetrieveAPIView):
#     # permission_classes = [
#     #     permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
#     queryset = Category.objects.all() 
#     serializer_class = CategorySerializer

class ApiRoot(APIView):
    def get(self, request, format=None):
        return Response({
            'users': reverse('users', request=request, format=format),
            'categories': reverse('categories', request=request, format=format),
            'posts': reverse('posts', request=request, format=format),
            'Create-category': reverse('category-create', request=request, format=format),
        })
        






# class PostList(APIView):
#     def get(self, request, format=None):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class PostDetail(APIView):
#     """
#     Retrieve, update or delete a code post.
#     """
#     def get_object(self, pk):
#         try:
#             return Post.objects.get(pk=pk)
#         except Post.DoesNotExist:
#             return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     def get(self, request, pk , format=None):
#         post= self.get_object(pk)
#         serializer = PostSerializer(post)
#         return  Response(serializer.data) 

#     def put(self, request, pk, format=None):
#         post = self.get_object(pk)
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return  Response(serializer.data)
#         return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         post = self.get_object(pk)
#         post.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def post_list(request, format=None):
#     """
#     List all code posts, or create a new post.
#     """
#     if request.method == 'GET':
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def post_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete a code post.
#     """
#     try:
#         post = Post.objects.get(pk=pk)
#     except Post.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = PostSerializer(post)
#         return Response(serializer.data)

#     elif request.method == 'PUT':

#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         post.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)
