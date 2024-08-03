from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import ProductForm


def list_view(request):
    return render(request, "products/list.html")


@login_required
def create_view(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()
            return redirect("products:list")
    else:
        form = ProductForm()
    return render(request, "products/create.html", {"form": form})
