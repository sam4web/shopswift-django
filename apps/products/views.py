from django.shortcuts import render


def list_view(request):
    return render(request, "products/list.html")
