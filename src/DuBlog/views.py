from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    title = "Homepage"
    user_name = request.user.get_username()
    if request.user.is_authenticated:
        context = {"user_name": user_name}
    else:
        context = {"user_name": "Anónimo"}
    return render(request, "home.html", context)


def about(request):
    title = "Acerca de"
    return render(request, "about.html")


def contact_us(request):
    title = "Contáctanos"
    return render(request, "contact_us.html")
