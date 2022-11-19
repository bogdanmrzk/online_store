from django.contrib import admin
from .models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "image",)
    list_display_links = ("name", "id")
    search_fields = ("name", "price")


@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    fields = ('category',)
    search_fields = ('category',)
