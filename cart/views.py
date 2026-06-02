from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from islamic_finance import cart
from users.models import User
from catalog.models import Product

from .models import Cart
from .models import CartItem

from .serializers import CartSerializer


class AddToCartView(APIView):

    def post(self, request):

        user_id = request.data.get("user_id")
        product_id = request.data.get("product_id")

        try:
            user = User.objects.get(id=user_id)

        except User.DoesNotExist:
            return Response(
                {"error": "Utilisateur introuvable"},
                status=404
            )

        try:
            product = Product.objects.get(id=product_id)

        except Product.DoesNotExist:
            return Response(
                {"error": "Produit introuvable"},
                status=404
            )

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

        return Response(
            {"message": "Ajouté au panier"}
        )
    

class CartDetailView(APIView):

    def get(self, request, user_id):

        try:
            cart = Cart.objects.get(
            user_id=user_id
            )

        except Cart.DoesNotExist:
            return Response(
            {"error": "Panier vide"},
            status=404
         )

        serializer = CartSerializer(cart)

        return Response(serializer.data)
    

