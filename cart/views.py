from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Cart, CartItem
from .serializers import (
    CartSerializer,
    CartItemSerializer
)

from produits.models import Produit
from users.models import User


class CartViewSet(viewsets.ModelViewSet):

    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemViewSet(viewsets.ModelViewSet):

    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    @action(
        detail=False,
        methods=["post"]
    )
    def add(self, request):

        user_id = request.data.get("user_id")
        product_id = request.data.get("product_id")

        user = User.objects.get(id=user_id)
        product = Produit.objects.get(id=product_id)

        cart, created = Cart.objects.get_or_create(
            user=user
        )

        item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product
        )

        if not created:
            item.quantite += 1
            item.save()

        return Response({
            "message": "Ajouté au panier"
        })