from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

User = settings.AUTH_USER_MODEL


class BlogPostQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        # BlogPost.objects
        return self.filter(publish_date__lte=now)

    def search(self, query):
        return self.filter(title__iexact=query)


class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self._db)

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().published().search(query)


class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    title = models.CharField(max_length=500)
    # Slug = Short URL Label (User Experience)
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True)
    publish_date = models.DateTimeField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    objects = BlogPostManager()

    # Ordering Newest to Oldest
    class Meta:
        ordering = ['-publish_date', '-updated', '-timestamp']

    def get_absolute_url(self):
        return f"/blog/{self.slug}"
