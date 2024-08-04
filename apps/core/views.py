from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from apps.cart.models import Cart, Order
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
        cart = get_object_or_404(Cart, customer=request.user)
        items = cart.products.all()
    except:
        return redirect("cart:cart")

    if request.method == "POST":
        order = Order.objects.create(
            name=request.POST.get("first-name"),
            address=request.POST.get("address"),
            customer=request.user,
        )
        order.products.set(items)
        Cart.objects.get(customer=request.user).delete()
        return redirect("product:list")

    pricing = {
        "sub_total": cart.get_total(),
        "shipping": 25,
        "tax": 14,
    }
    pricing["order_total"] = sum(pricing.values())
    context = {"pricing": pricing, "items": items}

    return render(request, "core/checkout.html", context)


@login_required
def orders_view(request):
    try:
        orders = Order.objects.filter(customer=request.user).order_by("-created_at")
    except Exception as e:
        print(e)
        return redirect("cart:cart")
    context = {"orders": orders}
    return render(request, "core/order.html", context)
