from . import views
from django.urls import path
from .views import (
    automobile_view,
    baby_products_view,
    health_and_beauty_view,
    fashion_view,
    gaming_view,
    other_categories_view,
    home_and_office_view,
    electronics_view,
    computing_view,
    phones_and_tablets_view,
    supermarket_view

)


urlpatterns = [
    path('', views.product_list, name='product_list'),
    path("search", views.search, name="search"),
    path("automobile/", automobile_view, name="automobile-view"),
    path("baby-products/", baby_products_view, name="baby-products"),
    path("health-and-beauty/", health_and_beauty_view, name="health-and-beauty"),
    path("fashion/", fashion_view, name="fashion"),
    path("gaming/", gaming_view, name="gaming"),
    path("other/", other_categories_view, name="other"),
    path("home-and-office/", home_and_office_view, name="home-and-office"),
    path("electronics/", electronics_view, name="electronics"),
    path("computing/", computing_view, name="computing"),
    path("supermarket/", supermarket_view, name="supermarket"),
    path("phones-and-tablets/", phones_and_tablets_view, name="phone-and-tablets"),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]