from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from .models import Cart, CartItem
from .serializers import (
    CartSerializer,
    CartItemSerializer
)

from produits.models import Produit


class CartViewSet(viewsets.ModelViewSet):

    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    @action(
        detail=False,
        methods=["get"]
    )
    def my_cart(self, request):

        user = request.user

        cart, created = Cart.objects.get_or_create(
            user=user
        )

        serializer = CartSerializer(cart)

        return Response(serializer.data)


class CartItemViewSet(viewsets.ModelViewSet):

    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    @action(
        detail=False,
        methods=["post"]
    )
    def add(self, request):

        product_id = request.data.get(
            "product_id"
        )

        try:

            product = Produit.objects.get(
                id=product_id
            )

        except Produit.DoesNotExist:

            return Response(
                {"error": "Produit introuvable"},
                status=404
            )

        user = request.user

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

    @action(
        detail=True,
        methods=["delete"]
    )
    def remove(self, request, pk=None):

        item = self.get_object()

        item.delete()

        return Response({
            "message": "Produit supprimé"
        })