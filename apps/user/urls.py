from django.urls import path

from .views import *

app_name = "user"

urlpatterns = [
    path("", profile_view, name="profile"),
    path("logout/", logout_view, name="logout"),
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
]
