from django.shortcuts import render

from apps.product.models import Product


def index_view(request):
    products = Product.objects.order_by("-updated_at")[:3]
    context = {"products": products}
    return render(request, "core/home.html", context=context)


def about_view(request):
    return render(request, "core/about.html")
