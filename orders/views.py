from rest_framework.views import APIView
from rest_framework.response import Response

from users.models import User
from cart.models import Cart
from cart.models import CartItem

from .models import Order
from .serializers import OrderSerializer


class CreateOrderView(APIView):

    def post(self, request):

        user_id = request.data.get(
            "user_id"
        )

        try:
            user = User.objects.get(
                id=user_id
            )

            cart = Cart.objects.get(
                user=user
            )

        except:
            return Response(
                {"error": "Panier introuvable"},
                status=404
            )

        items = CartItem.objects.filter(
            cart=cart
        )

        total = 0

        for item in items:
            total += item.total_price()

        order = Order.objects.create(
            user=user,
            cart=cart,
            total=total,
            statut="PENDING"
        )

        serializer = OrderSerializer(order)

        return Response(
            serializer.data
        )