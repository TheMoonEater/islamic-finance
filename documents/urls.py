from django.urls import path

from .views import (
    scoring_pdf_view,
    simulation_pdf_view
)

urlpatterns = [

    path(
        'documents/scoring/<int:scoring_id>/',
        scoring_pdf_view
    ),

    path(
        'documents/simulation/<int:simulation_id>/',
        simulation_pdf_view
    ),
]