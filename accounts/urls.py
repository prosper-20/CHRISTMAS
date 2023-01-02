from django.urls import path
from .views import register2

urlpatterns = [
    path("register", register2, name="register")
]