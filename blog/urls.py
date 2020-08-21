from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns
PostList = PostViewSet.as_view({
    'get': 'list',
    'posy': 'create'
})
PostDetail = PostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete':'destroy'
})

UserList = UserViewSet.as_view({
    'get': 'list'
})
UserDetail = UserViewSet.as_view({
    'get': 'retrieve'
})

CategoryList = CategoryViewSet.as_view({
    'get': 'list'
})
CategoryDetail = CategoryViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('', ApiRoot.as_view(), name="root"),
    
    path('category/', CategoryList, name= "categories"),
    path('category/create/', CategoryCreate.as_view(), name= "category-create"),
    path('category/<int:pk>/', CategoryDetail,name="single-category"),
    
    path('users/', UserList,name= "users"),
    path('users/<int:pk>/', UserDetail, name="single-user"),
    
    path('posts/',PostList, name="posts"),
    path('posts/<int:pk>/', PostDetail, name="single-post"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
