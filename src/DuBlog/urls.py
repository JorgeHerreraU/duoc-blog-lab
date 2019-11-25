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
from django.urls import path, include
from django.conf import settings

from django.conf.urls.static import static

from .views import home_page, contact_us, about

from blog.views import blog_post_create_item
from search.views import search_blog_post
from users.views import register, login, logout, edit_profile, change_password

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('contactanos/', contact_us),
    path('blog/', include('blog.urls')),
    path('search/', search_blog_post),
    path('login/', login),
    path('register/', register),
    path('logout/', logout),
    path('about/', about),
    path('edit_profile/', edit_profile),
    path('change_password/', change_password)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
