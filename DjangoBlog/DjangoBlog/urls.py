from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name='blog-admin'),
    path('', include('blog.urls')),
]

#govind00
#TestPassword