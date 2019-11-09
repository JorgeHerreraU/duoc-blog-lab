from django import forms


class ContactForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': "Nombre"
        }
    )
    )
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'placeholder': 'Email'
        }
    ))
    comentario = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Escribe tu mensaje aquí'}))

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if email.endswith(".tk"):
            raise forms.ValidationError(
                "Email inválido, dominio no permitido")
        return email
