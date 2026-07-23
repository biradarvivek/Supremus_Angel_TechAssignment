from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Cart


@login_required
def cart_page(request):
    cart = Cart.objects.filter(user=request.user).prefetch_related(
        "items__product"
    ).first()

    if not cart:
        context = {
            "cart": None,
            "total": 0,
        }
        return render(request, "cart/cart.html", context)

    total = sum(
        item.product.price * item.quantity
        for item in cart.items.all()
    )

    context = {
        "cart": cart,
        "total": total,
    }

    return render(request, "cart/cart.html", context)