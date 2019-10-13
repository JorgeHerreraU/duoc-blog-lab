from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import BlogPost


def blog_post_create_item(request):
    context = {"form": None}
    return render(request, 'blog_post_create.html', context)


def blog_post_get_all_items(request):
    """Returns a list of objects"""
    qs = BlogPost.objects.all()
    context = {"object_list": qs}
    return render(request, 'blog_post_list.html', context)


def blog_post_get_item(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    context = {"object": obj}
    return render(request, 'blog_post_detail.html', context)


def blog_post_update(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    context = {"object": obj, "form": None}
    return render(request, 'blog_post_update.html', context)


def blog_post_remove(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    context = {"object": obj}
    return render(request, 'blog_post_delete.html', context)
