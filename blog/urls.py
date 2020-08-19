from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('all/',PostList.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
