from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
from .models import BlogPost
from .forms import BlogPostFormModel


@staff_member_required
@login_required
def blog_post_create_item(request):
    """Create a new post"""
    title = "Nueva Publicación"
    form = BlogPostFormModel(request.POST or None)
    if form.is_valid():
        # Hookup the user to the blog post before saving
        post = form.save(commit=False)
        post.user = request.user
        # Save form
        post.save()
        # Clean form once saved
        form = BlogPostFormModel()
    context = {"title": title, "form": form}
    return render(request, 'blog/form.html', context)


def blog_post_get_all_items(request):
    """Returns a list of objects"""
    qs = BlogPost.objects.all()
    context = {"object_list": qs}
    return render(request, 'blog/list.html', context)


def blog_post_get_item(request, slug):
    """Returns an specific post"""
    obj = get_object_or_404(BlogPost, slug=slug)
    context = {"object": obj}
    return render(request, 'blog/details.html', context)


def blog_post_update(request, slug):
    # Lookup the BlogPost object
    obj = get_object_or_404(BlogPost, slug=slug)
    # Pass the specific form post to the BlogPostFormModel
    form = BlogPostFormModel(request.POST or None, instance=obj)
    # Save the new information
    if form.is_valid():
        form.save()
    context = {"form": form, "title": f'Actualizar {obj.title}'}
    return render(request, 'blog/form.html', context)


def blog_post_remove(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    context = {"object": obj}
    return render(request, 'blog/delete.html', context)
