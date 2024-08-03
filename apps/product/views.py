from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import ProductForm
from .models import Product


def list_view(request):
    products = Product.objects.order_by("-updated_at")
    context = {"products": products}
    return render(request, "product/list.html", context=context)


def detail_view(request, id):
    product = Product.objects.get(id=id)
    context = {"product": product}
    return render(request, "product/detail.html", context=context)


@login_required
def create_view(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()
            return redirect("product:list")
    else:
        form = ProductForm()

    context = {"form": form}
    return render(request, "product/create.html", context=context)
