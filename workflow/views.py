from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import BasePermission

from rest_framework.permissions import (
    IsAuthenticated
)

from users.permissions import (
    IsBankStaff
)

from .models import (
    DemandeFinancement,
    WorkflowHistory
)

from .serializers import (
    DemandeSerializer
)

from .services import (
    can_transition,
    can_validate
)

from clients.models import Client
from scoring.models import Scoring
from simulations.models import Simulation


class CreateDemandeView(APIView):

    def post(self, request):

        client_id = request.data.get(
            "client_id"
        )

        scoring_id = request.data.get(
            "scoring_id"
        )

        simulation_id = request.data.get(
            "simulation_id"
        )

        try:

            client = Client.objects.get(
                id=client_id
            )

            scoring = Scoring.objects.get(
                id=scoring_id
            )

            simulation = Simulation.objects.get(
                id=simulation_id
            )

        except Exception:
            return Response(
                {
                    "error": "Données invalides"
                },
                status=400
            )

        demande = DemandeFinancement.objects.create(
            client=client,
            scoring=scoring,
            simulation=simulation
        )

        serializer = DemandeSerializer(
            demande
        )

        return Response(serializer.data)


class ChangeStatusView(APIView):
    permission_classes = [
        IsAuthenticated,
        IsBankStaff
    ]

    def post(self, request):

        demande_id = request.data.get(
            "demande_id"
        )

        nouveau_statut = request.data.get(
            "nouveau_statut"
        )

        commentaire = request.data.get(
            "commentaire",
            ""
        )

        try:

            demande = DemandeFinancement.objects.get(
                id=demande_id
            )

        except DemandeFinancement.DoesNotExist:

            return Response(
                {
                    "error": "Demande introuvable"
                },
                status=404
            )

        ancien_statut = demande.statut

        if not can_transition(
            ancien_statut,
            nouveau_statut
        ):

            return Response(
                {
                    "error": "Transition invalide"
                },
                status=400
            )

        if not can_validate(
            request.user.role,
            nouveau_statut
        ):

            return Response(
                {
                    "error": "Permission refusée"
                },
                status=403
            )

        demande.statut = nouveau_statut
        demande.commentaire = commentaire
        demande.save()

        WorkflowHistory.objects.create(
            demande=demande,
            ancien_statut=ancien_statut,
            nouveau_statut=nouveau_statut,
            commentaire=commentaire
        )

        serializer = DemandeSerializer(
            demande
        )

        return Response(serializer.data)




