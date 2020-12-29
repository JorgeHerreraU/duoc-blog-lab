from django.db import models
from django.conf import settings
from django.utils import timezone
# Query library for complex search
from django.db.models import Q, Sum
# Create your models here.
from autoslug import AutoSlugField


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
    # Slug = Short URL Label
    slug = AutoSlugField(populate_from='title')
    content = models.TextField(null=True, blank=True)
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def upvote(self):
        return BlogPostUserReaction.objects.filter(blog_post=self).aggregate(Sum("upvote"))['upvote__sum']

    @property
    def downvote(self):
        return BlogPostUserReaction.objects.filter(blog_post=self).aggregate(Sum("downvote"))['downvote__sum']

    # This line is very important as it maps the objects to the default manager
    objects = BlogPostManager()

    # Ordering Newest to Oldest
    class Meta:
        ordering = ['-publish_date', '-updated', '-timestamp']

    def get_absolute_url(self):
        return f"/blog/{self.slug}"

    def get_slug(self):
        return self.slug


class BlogPostUserReaction(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upvote = models.SmallIntegerField(null=True, blank=True)
    downvote = models.SmallIntegerField(null=True, blank=True)


class BlogPostComment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)
