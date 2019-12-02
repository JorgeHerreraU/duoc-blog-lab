from django import forms
from .models import BlogPost


class BlogPostFormModel(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'image', 'content', 'publish_date']
        widgets = {
            "title": forms.TextInput(attrs={'placeholder': 'Titulo de la publicación'}),
            "image": forms.FileInput(),
            "slug": forms.TextInput(attrs={'placeholder': 'URL para la publicación'}),
            "content": forms.Textarea(attrs={'placeholder': 'Ingresa aquí el contenido de la publicación'}),
            "publish_date": forms.DateTimeInput(attrs={'placeholder': 'Formato: YYYY-MM-DD HH:MM:SS'}),
        }
        labels = {
            'title': 'Título',
            'image': 'Imagen',
            "slug": 'URL',
            'content': 'Contenido',
            'publish_date': 'Fecha de publicación'
        }

    def clean_title(self, *args, **kwargs):
        instance = self.instance
        title = self.cleaned_data.get('title')
        # Query to db and lookup for same title name
        qs = BlogPost.objects.filter(title__iexact=title)
        # Remove the instance to avoid the title validation if an instance exists
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError(
                "Este titulo ya ha sido utilizado. Por favor selecciona otro")
        return title
