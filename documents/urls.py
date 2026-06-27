from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    scoring_pdf_view,
    simulation_pdf_view,
    DocumentViewSet
)

router = DefaultRouter()

router.register(
    "documents",
    DocumentViewSet,
    basename="documents"
)

urlpatterns = [

    path(
        "documents/scoring/<int:scoring_id>/",
        scoring_pdf_view,
        name="scoring-pdf"
    ),

    path(
        "documents/simulation/<int:simulation_id>/",
        simulation_pdf_view,
        name="simulation-pdf"
    ),

    path(
        "",
        include(router.urls)
    ),
]