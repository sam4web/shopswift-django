from django.urls import path

from .views import *

app_name = "core"

urlpatterns = [
    path("", index_view, name="index"),
    path("about", about_view, name="about"),
    path("products", product_list, name="product_list"),
    path("login", login_view, name="login"),
    path("register", register_view, name="register"),
]
