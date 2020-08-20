from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('blog.urls')),
    path('api/', include('rest_framework.urls')),
]
