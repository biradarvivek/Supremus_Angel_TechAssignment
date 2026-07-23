from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from categories.models import Category
from .models import Product


def product_list(request):

    products = Product.objects.filter(
        is_active=True
    ).select_related("category")

    categories = Category.objects.all()

    search = request.GET.get("search")
    category = request.GET.get("category")

    if search:
        products = products.filter(
            name__icontains=search
        )

    if category:
        products = products.filter(
            category_id=category
        )

    paginator = Paginator(products, 8)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "products/list.html",
        {
            "page_obj": page_obj,
            "categories": categories,
            "selected_category": category,
            "search": search,
        },
    )

def product_detail(request, pk):
    product = get_object_or_404(
        Product.objects.select_related("category"),
        pk=pk,
        is_active=True,
    )

    related_products = Product.objects.filter(
        category=product.category,
        is_active=True,
    ).exclude(pk=product.pk)[:4]

    return render(
        request,
        "products/detail.html",
        {
            "product": product,
            "related_products": related_products,
        },
    )