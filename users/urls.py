from django.urls import path

from .views import (
    RegisterView,
    CustomTokenObtainPairView
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    path(
        'auth/register/',
        RegisterView.as_view()
    ),

    path(
        'auth/login/',
        CustomTokenObtainPairView.as_view()
    ),

    path(
        'auth/refresh/',
        TokenRefreshView.as_view()
    ),
]