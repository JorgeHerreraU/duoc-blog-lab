from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm


def home_page(request):
    title = "Inicio | DUOC UC Blog"
    user_name = request.user.get_username()
    if request.user.is_authenticated:
        context = {
            "user_name": user_name,
            "title": title
        }
    else:
        context = {"user_name": "Anónimo"}
    return render(request, "home.html", context)


def about(request):
    title = "Acerca de"
    context = {"title": title}
    return render(request, "about.html", context)


def contact_us(request):
    title = "Contáctanos"
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {"title": title, "form": form}
    return render(request, "contact_us.html", context)
