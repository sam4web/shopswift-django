from django.shortcuts import render


def index_view(request):
    return render(request, "core/home.html")


def about_view(request):
    return render(request, "core/about.html")


def login_view(request):
    return render(request, "user/login.html")


def register_view(request):
    return render(request, "user/register.html")


def product_list(request):
    return render(request, "products/list.html")
