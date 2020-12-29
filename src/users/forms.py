from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=150)

    class Meta:
        model = User
        fields = ('username', 'profile_picture', 'email', 'gender', 'password1', 'password2')
        labels = {
            'profile_picture': 'Foto de Perfil',
            'gender': 'Sexo'
        }


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'profile_picture', 'email', 'first_name', 'last_name')
