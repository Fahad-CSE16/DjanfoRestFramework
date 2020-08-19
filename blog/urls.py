from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('all/',post_list),
    path('<int:pk>/', post_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
