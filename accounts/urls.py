from django.urls import path
from .views import register, login, logout, login3

urlpatterns = [
    path("register", register, name="register"),
    path("login/", login, name="login"),
    path("login3/", login3, name="login3"),
    path("logout/", logout, name="logout")
]