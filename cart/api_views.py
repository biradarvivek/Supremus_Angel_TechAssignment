from django.shortcuts import get_object_or_404

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Product
from .models import Cart, CartItem
from .serializers import (
    CartSerializer,
    AddToCartSerializer,
    CartItemSerializer,
)

class CartView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        return cart

class AddToCartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):

        serializer = AddToCartSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product = get_object_or_404(
            Product,
            id=serializer.validated_data["product_id"],
            is_active=True,
        )

        quantity = serializer.validated_data["quantity"]

        if quantity > product.stock:
            return Response(
                {
                    "error": "Requested quantity exceeds available stock."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        cart, _ = Cart.objects.get_or_create(
            user=request.user
        )

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
        )

        if not created:
            new_quantity = cart_item.quantity + quantity

            if new_quantity > product.stock:
                return Response(
                    {
                        "error": "Requested quantity exceeds available stock."
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            cart_item.quantity = new_quantity

        else:
            cart_item.quantity = quantity

        cart_item.save()

        return Response(
            CartSerializer(cart).data,
            status=status.HTTP_200_OK,
        )

class UpdateCartItemView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):

        cart_item = get_object_or_404(
            CartItem,
            id=pk,
            cart__user=request.user,
        )

        quantity = request.data.get("quantity")

        if quantity is None:
            return Response(
                {
                    "error": "Quantity is required."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        quantity = int(quantity)

        if quantity < 1:
            return Response(
                {
                    "error": "Quantity must be at least 1."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        if quantity > cart_item.product.stock:
            return Response(
                {
                    "error": "Requested quantity exceeds available stock."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        cart_item.quantity = quantity
        cart_item.save()

        return Response(
            CartItemSerializer(cart_item).data
        )

class RemoveCartItemView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):

        cart_item = get_object_or_404(
            CartItem,
            id=pk,
            cart__user=request.user,
        )

        cart_item.delete()

        return Response(
            {
                "message": "Item removed successfully."
            },
            status=status.HTTP_204_NO_CONTENT,
        )