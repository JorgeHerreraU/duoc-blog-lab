from django.db import models
from django.conf import settings
from django.utils import timezone
# Query library for complex search
from django.db.models import Q
# Create your models here.

User = settings.AUTH_USER_MODEL


class BlogPostQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        # BlogPost.objects
        return self.filter(publish_date__lte=now)

    def search(self, query):
        lookup = (Q(title__icontains=query) | Q(
            content__icontains=query) | Q(user__first_name__icontains=query) | Q(user__username__icontains=query))
        return self.filter(lookup)


class BlogPostManager(models.Manager):
    def get_queryset(self):
        # Calling custom QuerySet methods from the manager
        # See more at django docs https://docs.djangoproject.com/en/2.2/topics/db/managers/
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

    # This line is very important as it maps the objects to the default manager
    objects = BlogPostManager()

    # Ordering Newest to Oldest
    class Meta:
        ordering = ['-publish_date', '-updated', '-timestamp']

    def get_absolute_url(self):
        return f"/blog/{self.slug}"
