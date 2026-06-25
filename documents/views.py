from django.http import HttpResponse


from scoring.models import Scoring
from simulations.models import Simulation

from .services import (
    generate_scoring_pdf,
    generate_simulation_pdf
)


def scoring_pdf_view(
    request,
    scoring_id
):

    scoring = Scoring.objects.get(
        id=scoring_id
    )

    is_client = (
    request.user.role == 'CLIENT'
    )

    pdf = generate_scoring_pdf(
    scoring,
    is_client=is_client
    )

    response = HttpResponse(
        pdf,
        content_type='application/pdf'
    )

    filename = (
    f"{scoring.client.nom}"
    f"{scoring.client.prenom}"
    f"Scoring.pdf"
  )

    response[
    'Content-Disposition'
] = f'attachment; filename="{filename}"'
    return response


def simulation_pdf_view(
    request,
    simulation_id
):

    simulation = Simulation.objects.get(
        id=simulation_id
    )

    pdf = generate_simulation_pdf(
        simulation
    )

    response = HttpResponse(
        pdf,
        content_type='application/pdf'
    )
    filename = (
    f"{simulation.client.nom}"
    f"{simulation.client.prenom}"
    f"Simulation.pdf"
)

    response[
    'Content-Disposition'
] = f'attachment; filename="{filename}"'


    return response




from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Document
from .serializers import DocumentSerializer


class DocumentViewSet(
    viewsets.ModelViewSet
):

    serializer_class = (
        DocumentSerializer
    )

    permission_classes = [
        IsAuthenticated
    ]

    def get_queryset(self):

        return Document.objects.filter(
            user=self.request.user
        )

    def perform_create(
        self,
        serializer
    ):

        serializer.save(
            user=self.request.user
        )