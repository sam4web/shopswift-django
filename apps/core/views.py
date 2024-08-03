from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.cart.models import Cart
from apps.product.models import Product


def index_view(request):
    products = Product.objects.order_by("-updated_at")[:3]
    context = {"products": products}
    return render(request, "core/home.html", context=context)


def about_view(request):
    return render(request, "core/about.html")


@login_required
def checkout_view(request):
    try:
        cart = Cart.objects.get(customer=request.user)
        pricing = {
            "sub_total": cart.get_total(),
            "shipping": 25,
            "tax": 14,
        }
        pricing["order_total"] = sum(pricing.values())
        context = {"pricing": pricing, "items": cart.products.all()}
    except:
        context = {}
    return render(request, "core/checkout.html", context)
