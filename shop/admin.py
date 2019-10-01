from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'create', 'update']
    list_filter = ['available', 'create', 'update']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
