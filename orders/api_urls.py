from django.urls import path

from .views import (
    CheckoutView,
    OrderHistoryView,
    OrderDetailView,
)

urlpatterns = [

    path(
        "checkout/",
        CheckoutView.as_view(),
        name="checkout",
    ),

    path(
        "",
        OrderHistoryView.as_view(),
        name="order-history",
    ),

    path(
        "<int:pk>/",
        OrderDetailView.as_view(),
        name="order-detail",
    ),
]