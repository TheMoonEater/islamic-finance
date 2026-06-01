from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from .serializers import (
    SimulationSerializer,
    SimulationInputSerializer
)

from clients.models import Client

from .models import Simulation
import simulations.serializers as serializers

from .services import (
    calcul_montant_finance,
    calcul_prix_final,
    calcul_mensualite
)


class CreateSimulationView(GenericAPIView):

    serializer_class = SimulationInputSerializer

    def post(self, request):

        client_id = request.data.get("client_id")

        prix_bien = float(
            request.data.get("prix_bien")
        )

        apport = float(
            request.data.get("apport")
        )

        marge = float(
            request.data.get("marge")
        )

        duree_mois = int(
            request.data.get("duree_mois")
        )

        try:
            client = Client.objects.get(
                id=client_id
            )

        except Client.DoesNotExist:
            return Response(
                {"error": "Client introuvable"},
                status=status.HTTP_404_NOT_FOUND
            )

        montant_finance = calcul_montant_finance(
            prix_bien,
            apport
        )

        prix_final = calcul_prix_final(
            montant_finance,
            marge
        )

        mensualite = calcul_mensualite(
            prix_final,
            duree_mois
        )

        simulation = Simulation.objects.create(
            client=client,
            prix_bien=prix_bien,
            apport=apport,
            montant_finance=montant_finance,
            marge=marge,
            prix_final=prix_final,
            duree_mois=duree_mois,
            mensualite=mensualite
        )

        serializer = serializers.SimulationSerializer(
            simulation
            )

        return Response(serializer.data)