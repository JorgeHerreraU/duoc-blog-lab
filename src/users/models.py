from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
	GENDER_MALE = 0
	GENDER_FEMALE = 1
	GENDER_CHOICES = [(GENDER_MALE, 'Hombre'), (GENDER_FEMALE, 'Mujer')]
	gender = models.IntegerField(choices=GENDER_CHOICES, null=True, blank=True)
	profile_picture = models.ImageField(upload_to='profile/', blank=True, null=True)
