from django.shortcuts import render
from blog.models import BlogPost
from .models import SearchQuery
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def search_blog_post(request):
    # Default will be None
    query = request.GET.get('q', None)
    user = None
    context = {'query': query}
    if request.user.is_authenticated:
        user = request.user
    if query is not None:
        SearchQuery.objects.create(user=user, query=query)
        blog_list = BlogPost.objects.search(query=query)
        context['blog_list'] = blog_list

    return render(request, 'search/search.html', context)
