from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from apps.product.models import Product
from .models import Cart


@login_required
def cart_view(request):
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
    return render(request, "core/cart.html", context)


@login_required
def add_view(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        try:
            cart = Cart.objects.get(customer=request.user)
        except:
            cart = Cart.objects.create(customer=request.user)
        finally:
            cart.products.add(product)
    except:
        pass
    return redirect("cart:cart")


@login_required
def remove_view(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        cart = Cart.objects.get(customer=request.user)
        cart.products.remove(product)
    except:
        pass
    return redirect("cart:cart")
