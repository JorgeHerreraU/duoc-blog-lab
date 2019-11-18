from django import forms
from .models import BlogPost


# class BlogPostForm(forms.Form):
#     title = forms.CharField(widget=forms.TextInput(
#         attrs={
#             "placeholder": "Título"
#         }
#     ))
#     slug = forms.SlugField(widget=forms.TextInput(
#         attrs={
#             "placeholder": "Slug"
#         }
#     ))
#     content = forms.CharField(widget=forms.Textarea(
#         attrs={
#             "placeholder": "Escribe tu historia aquí"
#         }
#     ))


class BlogPostFormModel(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'image', 'content', 'publish_date']
        widgets = {
            "title": forms.TextInput(attrs={'placeholder': 'Ej: Mi canción preferida'}),
            "slug": forms.TextInput(attrs={'placeholder': 'Ej: cancion-preferida'}),
            "content": forms.Textarea(attrs={'placeholder': 'Ej: Me gusta pneuma de tool'}),
            "publish_date": forms.DateTimeInput(attrs={'placeholder': 'Ej: 2019-15-19 12:30:00'}),
        }
        labels = {
            'title': 'Título',
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
