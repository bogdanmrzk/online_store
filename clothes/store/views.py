from django.shortcuts import render, get_list_or_404
from .models import *


def basic_view(request):
    all_products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'clothes/index.html', context={'items': all_products,
                                                          'categories': categories})


def category_list(request, category_v):
    categories = Category.objects.all()
    categories_filter = Product.objects.filter(category_name__category=category_v)
    return render(request, 'clothes/category_filter.html', context={
                                                            'categories_filter': categories_filter,
                                                            'categories': categories})

