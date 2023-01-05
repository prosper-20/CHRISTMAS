from . import views
from django.urls import path
from .views import automobile_view


urlpatterns = [
    path('', views.product_list, name='product_list'),
    path("search", views.search, name="search"),
    path("automobile/", automobile_view, name="automobile-view"),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]