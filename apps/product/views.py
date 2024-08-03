from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect

from .forms import ProductForm
from .models import Product, CATEGORIES
from .utils import filtered_products


def list_view(request):
    products, url_query = filtered_products(request)
    context = {"products": products, "categories": CATEGORIES, "url_query": url_query}
    return render(request, "product/list.html", context)


def detail_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
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


@login_required
def delete_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if product.created_by == request.user:
        product.delete()
    return redirect("product:list")


@login_required
def edit_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if product.created_by != request.user:
        return redirect("product:list")

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product.save()
            return redirect("product:list")
    else:
        form = ProductForm(instance=product)

    context = {"form": form}
    return render(request, "product/update.html", context)
