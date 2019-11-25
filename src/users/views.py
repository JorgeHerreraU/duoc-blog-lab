from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout, login as do_login, authenticate, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm


# Create your views here.


def register(request):
    form = UserCreationForm()
    form.fields['username'].widget.attrs.update({
        'placeholder': 'Nombre de usuario'
    })
    form.fields['password1'].widget.attrs.update({
        'placeholder': 'Ingresar contraseña'
    })
    form.fields['password2'].widget.attrs.update({
        'placeholder': 'Repetir contraseña'
    })
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                do_login(request, user)
                return redirect('/')
    return render(request, "users/register.html", {'form': form})


def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                do_login(request, user)
                return redirect('/')
    return render(request, "users/login.html", {'form': form})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(
            instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return render(request, "users/profile.html", {'form': form})
    else:
        form = UserProfileForm(instance=request.user)
        return render(request, "users/profile.html", {'form': form})


def logout(request):
    do_logout(request)
    return redirect('/')


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(
                request, 'La contraseña se ha actualizado exitosamente!')
            return redirect('change_password')
        else:
            messages.error(
                request, 'Por favor corregir el error de más abajo.')
    else:
        form = PasswordChangeForm(request.user)

    form.fields['old_password'].widget.attrs.update({
        'placeholder': 'Ingresar contraseña antigua'
    })
    form.fields['new_password1'].widget.attrs.update({
        'placeholder': 'Ingresar contraseña nueva'
    })
    form.fields['new_password2'].widget.attrs.update({
        'placeholder': 'Repetir contraseña nueva'
    })
    return render(request, 'users/change_password.html', {
        'form': form
    })
