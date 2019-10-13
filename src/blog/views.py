from django.shortcuts import render

# Create your views here.
from .models import BlogPost


def blog_post_detail_page(request):
    obj = BlogPost.objects.get(id=1)
    context = {"object": obj}
    return render(request, 'blog_post_detail.html', context)
