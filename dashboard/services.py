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
from produits.models import Produit
from django.db.models.functions import TruncMonth
from django.db.models import Count


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

def simulations_by_month():

    data = (
        Simulation.objects
        .annotate(month=TruncMonth("created_at"))
        .values("month")
        .annotate(total=Count("id"))
        .order_by("month")
    )

    return [
        {
            "mois": item["month"].strftime("%m/%Y"),
            "total": item["total"]
        }
        for item in data
    ]


def scoring_decisions():

    return {
        "ELIGIBLE": Scoring.objects.filter(
            decision="ELIGIBLE"
        ).count(),

        "A_ANALYSER": Scoring.objects.filter(
            decision="A_ANALYSER"
        ).count(),

        "REFUSE": Scoring.objects.filter(
            decision="REFUSE"
        ).count()
    }


def products_by_category():

    data = (
        Produit.objects
        .values("category")
        .annotate(total=Count("id"))
    )

    return list(data)



def last_demands():

    simulations = (
        Simulation.objects
        .select_related("client")
        .order_by("-created_at")[:5]
    )

    return [

        {
            "client":
            f"{s.client.prenom} {s.client.nom}",

            "montant":
            s.montant_finance,

            "date":
            s.created_at.strftime("%d/%m/%Y")
        }

        for s in simulations
    ]


def last_clients():

    clients = (
        Client.objects
        .order_by("-created_at")[:5]
    )

    return [

        {

            "nom":
            f"{c.prenom} {c.nom}",

            "date":
            c.created_at.strftime("%d/%m/%Y")

        }

        for c in clients

    ]



def dashboard_charts():

    return {

        "stats": get_dashboard_stats(),

        "workflow": demandes_by_status(),

        "simulations_par_mois": simulations_by_month(),

        "scoring": scoring_decisions(),

        "categories": products_by_category(),

        "dernieres_demandes": last_demands(),

        "derniers_clients": last_clients(),

    }


