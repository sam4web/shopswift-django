from django.db.models import Q

from .models import Product


def filtered_products(request):
    products = Product.objects.order_by("-updated_at")
    url_query = {}
    if len(request.GET) > 0:
        name = request.GET["name"]
        category = int(request.GET["category"])
        sort = request.GET["sort"]
        min_price = int(request.GET["min"]) if request.GET["min"] else None
        max_price = int(request.GET["max"]) if request.GET["max"] else None

        if name:
            products = Product.objects.filter(Q(name__icontains=name))
            url_query["name"] = name

        if category > 0:
            products = products.filter(Q(category=category))
            url_query["category"] = category

        if min_price:
            products = products.filter(Q(price__gte=min_price))
            url_query["min"] = min_price
        if max_price:
            products = products.filter(Q(price__lte=max_price))
            url_query["max"] = max_price

        url_query["sort"] = sort
        if sort == "low":
            products = products.order_by("price")
        elif sort == "high":
            products = products.order_by("-price")
        elif sort == "order":
            products = products.order_by("name")
        elif sort == "reverse":
            products = products.order_by("-name")
    return products, url_query
