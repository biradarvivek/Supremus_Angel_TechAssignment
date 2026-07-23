from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart
from django.contrib import messages

from products.models import Product
from .models import Cart, CartItem
from django.views.decorators.http import require_POST

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


@login_required
def add_to_cart(request, product_id):
    print("===== HTML add_to_cart view called =====")
    product = get_object_or_404(
        Product,
        id=product_id,
        is_active=True,
    )

    quantity = int(request.POST.get("quantity", 1))

    if quantity > product.stock:
        messages.error(
            request,
            "Requested quantity exceeds available stock."
        )
        return redirect("product-detail", pk=product.id)

    cart, _ = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
    )

    if created:
        cart_item.quantity = quantity
    else:
        if cart_item.quantity + quantity > product.stock:
            messages.error(
                request,
                "Requested quantity exceeds available stock."
            )
            return redirect("product-detail", pk=product.id)

        cart_item.quantity += quantity

    cart_item.save()

    messages.success(
        request,
        f"{product.name} added to your cart."
    )

    return redirect("cart-page")

@login_required
@require_POST
def update_cart_item(request, item_id):

    cart_item = get_object_or_404(
        CartItem,
        id=item_id,
        cart__user=request.user,
    )

    action = request.POST.get("action")

    if action == "increase":

        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
            cart_item.save()
        else:
            messages.warning(
                request,
                "Maximum stock reached."
            )

    elif action == "decrease":

        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()

    return redirect("cart-page")

@login_required
@require_POST
def remove_cart_item(request, item_id):

    cart_item = get_object_or_404(
        CartItem,
        id=item_id,
        cart__user=request.user,
    )

    cart_item.delete()

    messages.success(
        request,
        "Item removed from cart."
    )

    return redirect("cart-page")