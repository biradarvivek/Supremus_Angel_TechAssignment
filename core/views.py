from django.shortcuts import render
from products.models import Product
from categories.models import Category


def home(request):

    featured_products = Product.objects.filter(
        is_active=True
    )[:8]

    categories = Category.objects.all()

    context = {
        "featured_products": featured_products,
        "categories": categories,
    }

    return render(
        request,
        "home.html",
        context,
    )