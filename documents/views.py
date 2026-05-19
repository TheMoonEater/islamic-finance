from django.http import HttpResponse

from islamic_finance import scoring
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