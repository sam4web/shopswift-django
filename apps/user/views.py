from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def profile_view(request):
    return render(request, "user/profile.html")


@login_required
def logout_view(request):
    logout(request)
    return redirect("user:login")


def login_view(request):
    return render(request, "user/login.html")


def register_view(request):
    return render(request, "user/register.html")
