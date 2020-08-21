from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('', ApiRoot.as_view(), name="root"),
    
    path('category/', CategoryList.as_view(), name= "categories"),
    path('category/create/', CategoryCreate.as_view(), name= "category-create"),
    path('category/<int:pk>/', CategoryDetail.as_view(),name="single-category"),
    
    path('users/', UserList.as_view(),name= "users"),
    path('users/<int:pk>/', UserDetail.as_view(), name="single-user"),
    
    path('posts/',PostList.as_view(), name="posts"),
    path('posts/<int:pk>/', PostDetail.as_view(), name="single-post"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
