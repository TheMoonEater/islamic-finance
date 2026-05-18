from django.urls import path

from .views import (
    CreateDemandeView,
    ChangeStatusView
)

urlpatterns = [

    path(
        'demandes/create/',
        CreateDemandeView.as_view()
    ),

    path(
        'demandes/change-status/',
        ChangeStatusView.as_view()
    ),
]