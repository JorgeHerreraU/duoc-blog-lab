from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import BlogPost
from .forms import BlogPostForm, BlogPostFormModel


def blog_post_create_item(request):
    title = "Nueva Publicación"
    form = BlogPostFormModel(request.POST or None)
    if form.is_valid():
        form.save()
        # Clean Form
        form = BlogPostFormModel()
    context = {"title": title, "form": form}
    return render(request, 'blog/form.html', context)


def blog_post_get_all_items(request):
    """Returns a list of objects"""
    qs = BlogPost.objects.all()
    context = {"object_list": qs}
    return render(request, 'blog/list.html', context)


def blog_post_get_item(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    context = {"object": obj}
    return render(request, 'blog/details.html', context)


def blog_post_update(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    context = {"object": obj, "form": None}
    return render(request, 'blog/update.html', context)


def blog_post_remove(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    context = {"object": obj}
    return render(request, 'blog/delete.html', context)
