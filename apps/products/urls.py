from django.urls import path

from .views import *

app_name = "products"

urlpatterns = [
    path("", list_view, name="list"),
]
