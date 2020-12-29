from django.contrib import admin

# Register your models here.
from .models import BlogPost, BlogPostUserReaction, BlogPostComment

admin.site.register(BlogPost)
admin.site.register(BlogPostUserReaction)
admin.site.register(BlogPostComment)