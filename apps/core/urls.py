from django.urls import path

from .views import *

app_name = "core"

urlpatterns = [
    path("", index_view, name="index"),
    path("about/", about_view, name="about"),
    path("checkout/", checkout_view, name="checkout"),
]
