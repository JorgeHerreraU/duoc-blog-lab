from django.db import models

# Create your models here.


class BlogPost(models.Model):
    title = models.TextField()
    # Short URL Label (User Experience)
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True)
