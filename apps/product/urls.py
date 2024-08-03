from django.urls import path

from .views import *

app_name = "product"

urlpatterns = [
    path("", list_view, name="list"),
    path("<str:id>/", detail_view, name="detail"),
    path("create/", create_view, name="create"),
]
