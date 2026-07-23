from django.urls import path

from .views import (
    checkout_page,
    order_history,
    order_detail,
)

urlpatterns = [

    path(
        "",
        order_history,
        name="order-history-page",
    ),

    path(
        "checkout/",
        checkout_page,
        name="checkout-page",
    ),

    path(
        "<int:order_id>/",
        order_detail,
        name="order-detail-page",
    ),
]