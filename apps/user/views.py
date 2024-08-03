from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from .forms import RegistrationForm


@login_required
def profile_view(request):
    context = {"user": request.user, "products": request.user.products.all()}
    return render(request, "user/profile.html", context=context)


@login_required
def logout_view(request):
    logout(request)
    return redirect("user:login")


def login_view(request):
    if request.user.is_authenticated:
        return redirect("core:index")
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("core:index")
    else:
        form = AuthenticationForm()
    return render(request, "user/login.html", {"form": form})


def register_view(request):
    if request.user.is_authenticated:
        return redirect("core:index")

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("core:index")
    else:
        form = RegistrationForm()
    return render(request, "user/register.html", {"form": form})
