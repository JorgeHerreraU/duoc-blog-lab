from django import forms

from .models import BlogPost


class BlogPostForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder": "Título"
        }
    ))
    slug = forms.SlugField(widget=forms.TextInput(
        attrs={
            "placeholder": "Slug"
        }
    ))
    content = forms.CharField(widget=forms.Textarea(
        attrs={
            "placeholder": "Escribe tu historia aquí"
        }
    ))


class BlogPostFormModel(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'
        widgets = {
            "title": forms.TextInput(attrs={'placeholder': 'Nombre'}),
            "slug": forms.TextInput(attrs={'placeholder': 'Slug'}),
            "content": forms.Textarea(attrs={'placeholder': 'Escribe tu contenido aquí'})
        }
