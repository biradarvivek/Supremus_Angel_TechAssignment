from django.urls import path

from .api_views import (
    CartView,
    AddToCartView,
    UpdateCartItemView,
    RemoveCartItemView,
)

urlpatterns = [
    path("", CartView.as_view(), name="cart"),

    path("add/", AddToCartView.as_view(), name="add-to-cart"),

    path(
        "items/<int:pk>/",
        UpdateCartItemView.as_view(),
        name="update-cart-item",
    ),

    path(
        "items/<int:pk>/delete/",
        RemoveCartItemView.as_view(),
        name="remove-cart-item",
    ),
]