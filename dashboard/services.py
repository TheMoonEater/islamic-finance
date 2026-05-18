from clients.models import Client

from workflow.models import (
    DemandeFinancement
)

from scoring.models import Scoring

from simulations.models import (
    Simulation
)

from django.db.models import Avg
from django.db.models import Sum


def get_dashboard_stats():

    total_clients = Client.objects.count()

    total_demandes = (
        DemandeFinancement.objects.count()
    )

    accepted = (
        DemandeFinancement.objects.filter(
            statut='ACCEPTE'
        ).count()
    )

    refused = (
        DemandeFinancement.objects.filter(
            statut='REFUSE'
        ).count()
    )

    total_financed = (
        Simulation.objects.aggregate(
            Sum('montant_finance')
        )['montant_finance__sum']
        or 0
    )

    average_score = (
        Scoring.objects.aggregate(
            Avg('score')
        )['score__avg']
        or 0
    )

    acceptance_rate = 0

    if total_demandes > 0:

        acceptance_rate = (
            accepted / total_demandes
        ) * 100

    return {

        "total_clients": total_clients,

        "total_demandes": total_demandes,

        "accepted": accepted,

        "refused": refused,

        "total_financed": total_financed,

        "average_score": round(
            average_score,
            2
        ),

        "acceptance_rate": round(
            acceptance_rate,
            2
        )
    }


from collections import Counter


def demandes_by_status():

    demandes = (
        DemandeFinancement.objects.all()
    )

    statuts = [
        d.statut
        for d in demandes
    ]

    return Counter(statuts)