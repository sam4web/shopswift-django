from django.shortcuts import render

from apps.product.models import Product


def index_view(request):
    products = Product.objects.order_by("-updated_at")[:3]
    context = {"products": products}
    return render(request, "core/home.html", context=context)


def about_view(request):
    return render(request, "core/about.html")


def login_view(request):
    return render(request, "user/login.html")


def register_view(request):
    return render(request, "user/register.html")


def product_list(request):
    return render(request, "product/list.html")
