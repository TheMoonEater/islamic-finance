from rest_framework import serializers

from .models import Cart
from .models import CartItem


class CartItemSerializer(serializers.ModelSerializer):

        product_name = serializers.CharField(
        source="product.nom",
        read_only=True
    )

        class Meta:
            model = CartItem
            fields = '__all__'


class CartSerializer(serializers.ModelSerializer):

    items = CartItemSerializer(
        source='cartitem_set',
        many=True,
        read_only=True
    )

    class Meta:
        model = Cart
        fields = '__all__'