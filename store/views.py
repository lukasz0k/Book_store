from django.shortcuts import render, get_object_or_404
from .models import Category, Product


# Create your views here.
def products(request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'home.html', {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'detail.html', {'product': product})


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'category.html', {'category': category, 'products': products})
