from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.


class UserTest(TestCase):

    def test_save_user(self):
        self.user = get_user_model().objects.create_user(
            username='test', password='12test12', email='test@example.com')
        self.user.save()
