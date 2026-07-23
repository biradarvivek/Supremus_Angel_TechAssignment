from django.db import transaction

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.models import Cart, CartItem

from .models import Order, OrderItem
from .serializers import (
    CheckoutSerializer,
    OrderSerializer,
)

class CheckoutView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    @transaction.atomic
    def post(self, request):

        serializer = CheckoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        cart = Cart.objects.filter(
            user=request.user
        ).first()

        if not cart or not cart.items.exists():

            return Response(
                {
                    "error": "Your cart is empty."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        cart_items = cart.items.select_related("product")

        total = 0

        for item in cart_items:

            if item.quantity > item.product.stock:

                return Response(
                    {
                        "error": f"{item.product.name} is out of stock."
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            total += item.quantity * item.product.price

        order = Order.objects.create(
            user=request.user,
            shipping_address=serializer.validated_data[
                "shipping_address"
            ],
            payment_method=serializer.validated_data[
                "payment_method"
            ],
            total_price=total,
        )

        for item in cart_items:

            OrderItem.objects.create(
                order=order,
                product=item.product,
                price=item.product.price,
                quantity=item.quantity,
            )

            item.product.stock -= item.quantity
            item.product.save()

        cart_items.delete()

        return Response(
            OrderSerializer(order).data,
            status=status.HTTP_201_CREATED,
        )

class OrderHistoryView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return (
            Order.objects.filter(user=self.request.user)
            .prefetch_related("items__product")
            .order_by("-created_at")
        )
class OrderDetailView(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return (
            Order.objects.filter(user=self.request.user)
            .prefetch_related("items__product")
        )