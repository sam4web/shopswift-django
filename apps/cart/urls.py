from django.urls import path

from .views import *

app_name = "cart"

urlpatterns = [
    path("", cart_view, name="cart"),
    path("add/<str:product_id>", add_view, name="add"),
    path("remove/<str:product_id>", remove_view, name="remove"),
]
