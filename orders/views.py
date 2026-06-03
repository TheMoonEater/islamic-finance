from rest_framework import viewsets

from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Order
from .serializers import OrderSerializer

from cart.models import Cart


class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(
        detail=False,
        methods=["post"]
    )
    def create_from_cart(self, request):

        cart_id = request.data.get("cart_id")

        cart = Cart.objects.get(
            id=cart_id
        )

        total = 0

        for item in cart.cartitem_set.all():

            total += (
                item.product.prix
                * item.quantite
            )

        order = Order.objects.create(
            user=cart.user,
            cart=cart,
            total=total
        )

        serializer = OrderSerializer(
            order
        )

        return Response(
            serializer.data
        )