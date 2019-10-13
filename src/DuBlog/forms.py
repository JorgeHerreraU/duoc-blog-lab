from django import forms


class ContactForm(forms.Form):
    nombre = forms.CharField()
    email = forms.EmailField()
    comentario = forms.CharField(widget=forms.Textarea)
