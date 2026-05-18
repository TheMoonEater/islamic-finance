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

    pdf = generate_scoring_pdf(
        scoring
    )

    response = HttpResponse(
        pdf,
        content_type='application/pdf'
    )

    response[
        'Content-Disposition'
    ] = 'attachment; filename="scoring.pdf"'

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

    response[
        'Content-Disposition'
    ] = 'attachment; filename="simulation.pdf"'

    return response