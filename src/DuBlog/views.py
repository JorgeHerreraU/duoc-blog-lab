from django.shortcuts import render, redirect
from .forms import ContactForm
from blog.models import BlogPost


def home_page(request):
    title = "Inicio"
    user_name = request.user.get_username()
    qs = BlogPost.objects.all()[:3]
    if request.user.is_authenticated:
        context = {
            "user_name": user_name,
            "title": title,
            "blog_list": qs
        }
        return render(request, "home.html", context)
    else:
        return redirect('/login')


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
