from django.urls import path

from .views import AddToCartView
from .views import CartDetailView

urlpatterns = [

    path(
        'cart/add/',
        AddToCartView.as_view()
    ),

    path(
        'cart/<int:user_id>/',
        CartDetailView.as_view()
    ),
]