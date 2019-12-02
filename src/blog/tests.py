from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import BlogPost


# Create your tests here.

class BlogPostTest(TestCase):
    def test_create_blog_post(self):
        user = get_user_model().objects.create_user(
            username='test', password='12test12', email='test@example.com')
        BlogPost.objects.create(
            user=user,
            image=None,
            title="Titulo de prueba",
            slug="titulo-prueba",
            content="Contenido de prueba"
        )
