from django.contrib import admin
from .models import Category, Product, Brand


admin.site.register(Brand)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
    'available', 'created', 'updated', 'latest', 'limited_stock', 'top_rated']
    list_filter = ['available', 'created', 'updated', 'limited_stock', 'top_rated']
    list_editable = ['price', 'available', 'latest', 'limited_stock', 'top_rated']
    prepopulated_fields = {'slug': ('name',)}
