from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import redirect, render, get_object_or_404

from cart.models import Cart
from .models import Order, OrderItem

@login_required
def checkout_page(request):

    cart = Cart.objects.filter(
        user=request.user
    ).prefetch_related(
        "items__product"
    ).first()

    if not cart or not cart.items.exists():
        messages.warning(request, "Your cart is empty.")
        return redirect("cart-page")

    total = sum(item.subtotal for item in cart.items.all())

    if request.method == "POST":

        shipping_address = request.POST.get("shipping_address")

        if not shipping_address:
            messages.error(request, "Shipping address is required.")
            return redirect("checkout-page")

        with transaction.atomic():

            order = Order.objects.create(
                user=request.user,
                shipping_address=shipping_address,
                total_price=total,
                payment_method="COD",
            )

            for item in cart.items.all():

                if item.quantity > item.product.stock:

                    messages.error(
                        request,
                        f"{item.product.name} is out of stock."
                    )

                    return redirect("cart-page")

                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    price=item.product.price,
                    quantity=item.quantity,
                )

                item.product.stock -= item.quantity
                item.product.save()

            cart.items.all().delete()

        messages.success(
            request,
            "Order placed successfully."
        )

        return redirect("order-history-page")

    return render(
        request,
        "orders/checkout.html",
        {
            "cart": cart,
            "total": total,
        },
    )


@login_required
def order_history(request):

    orders = (
        Order.objects.filter(user=request.user)
        .prefetch_related("items__product")
        .order_by("-created_at")
    )

    return render(
        request,
        "orders/order_history.html",
        {
            "orders": orders,
        },
    )


@login_required
def order_detail(request, order_id):

    order = get_object_or_404(
        Order.objects.prefetch_related("items__product"),
        id=order_id,
        user=request.user,
    )

    return render(
        request,
        "orders/order_detail.html",
        {
            "order": order,
        },
    )