from django.urls import path

from .views import *

app_name = "product"

urlpatterns = [
    path("", list_view, name="list"),
    path("create/", create_view, name="create"),
    path("delete/<str:product_id>/", delete_view, name="delete"),
    path("<str:product_id>/", detail_view, name="detail"),
]
