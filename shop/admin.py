from django.contrib import admin
from .models import Category, Product, Brand
from parler.admin import TranslatableAdmin


admin.site.register(Brand)


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ['name', 'slug']
    
    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(TranslatableAdmin):
    list_display = ['name', 'slug', 'price',
    'available', 'created', 'updated', 'latest', 'limited_stock', 'top_rated']
    list_filter = ['available', 'created', 'updated', 'limited_stock', 'top_rated']
    list_editable = ['price', 'available', 'latest', 'limited_stock', 'top_rated']
    
    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}





