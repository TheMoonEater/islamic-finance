from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    ClientViewSet,
    DebugAuthView,
    DebugJWTView
)

router = DefaultRouter()

router.register(
    "clients",
    ClientViewSet
)

urlpatterns = [

    path(
        "debug-auth/",
        DebugAuthView.as_view()
    ),

    
    path(
        "debug-jwt/",
        DebugJWTView.as_view()
    ),

    


    path(
        "",
        include(router.urls)
    ),
]






