"""DuBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views import home_page

from blog.views import blog_post_get_item, blog_post_get_all_items, blog_post_create_item, blog_post_remove, blog_post_update

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('blog/', blog_post_get_all_items),
    path('blog/create/', blog_post_create_item),
    path('blog/details/<str:slug>/', blog_post_get_item),
    path('blog/details/<str:slug>/edit', blog_post_update),
    path('blog/details/<str:slug>/remove', blog_post_remove),
]
