from django.urls import path

from .views import (
    cart_page,
    add_to_cart,
    update_cart_item,
    remove_cart_item,
)

urlpatterns = [

    path(
        "",
        cart_page,
        name="cart-page",
    ),

    path(
        "add/<int:product_id>/",
        add_to_cart,
        name="add-to-cart-page",
    ),

    path(
        "update/<int:item_id>/",
        update_cart_item,
        name="update-cart-item-page",
    ),

    path(
        "remove/<int:item_id>/",
        remove_cart_item,
        name="remove-cart-item-page",
    ),

]