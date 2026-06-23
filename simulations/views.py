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
    calcul_salaire_total,
    calcul_ce_brute,
    calcul_ce_nette,
    calcul_apport_minimum,
    calcul_montant_finance,
    calcul_prix_final,
    calcul_mensualite,
    calcul_total_marge,
    calcul_total_tva
)


class CreateSimulationView(GenericAPIView):

    serializer_class = SimulationInputSerializer

    def post(self, request):

        client_id = request.data.get("client_id")

        prix_bien = float(
            request.data.get("prix_bien")
        )

        salaire_acheteur = float(
            request.data.get(
                "salaire_acheteur"
            )
        )
        
        salaire_co_acheteur = float(
            request.data.get(
                "salaire_co_acheteur",
                0
            )
        )

        credit_consomme = float(
            request.data.get(
                "credit_consomme",
                0
            )
        )

        apport = float(
            request.data.get("apport")
        )

        marge = float(
            request.data.get(
                "marge",
                30
            )
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

        # ======================
        # CALCULS
        # ======================

        salaire_total = calcul_salaire_total(
            salaire_acheteur,
            salaire_co_acheteur
        )

        ce_brute = calcul_ce_brute(
            salaire_total
        )

        ce_nette = calcul_ce_nette(
            ce_brute,
            credit_consomme
        )

        apport = calcul_apport_minimum(
            prix_bien,
            ce_nette,
            duree_mois
        )

        montant_finance = (
            calcul_montant_finance(
                prix_bien,
                apport
            )
        )

        prix_final = (
            calcul_prix_final(
                montant_finance,
                marge
            )
        )

        mensualite = (
            calcul_mensualite(
                prix_final,
                duree_mois
            )
        )

        montant_total_marge = (
            calcul_total_marge(
                montant_finance,
                marge
            )
        )

        montant_total_tva = (
            calcul_total_tva(
                montant_total_marge
            )
        )

        montant_remboursement = (
            montant_finance
            + montant_total_marge
            + montant_total_tva
        )

        # ======================
        # SAUVEGARDE
        # ======================

        simulation = Simulation.objects.create(

            client=client,

            prix_bien=prix_bien,

            salaire_acheteur=salaire_acheteur,

            salaire_co_acheteur=
            salaire_co_acheteur,

            salaire_total=
            salaire_total,

            ce_brute=ce_brute,

            credit_consomme=
            credit_consomme,

            ce_nette=ce_nette,

            apport=apport,

            montant_finance=
            montant_finance,

            marge=marge,

            prix_final=
            prix_final,

            duree_mois=
            duree_mois,

            mensualite=
            mensualite,

            montant_remboursement=
            montant_remboursement,

            montant_total_marge=
            montant_total_marge,

            montant_total_tva=
            montant_total_tva
        )

        serializer = (
            serializers.SimulationSerializer(
                simulation
            )
        )

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )