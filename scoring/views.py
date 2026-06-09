from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from scoring_config.models import (
    ScoringConfig
)

from .serializers import ScoringSerializer


class CalculateScoringView(generics.GenericAPIView):

    serializer_class = ScoringSerializer

    def post(self, request):

        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        score = 0

        # salaire
        config = ScoringConfig.objects.first()

        if not config:
            config = ScoringConfig.objects.create()

        if data["salaire"] >= 100000:
            score += config.salaire_100k

        elif data["salaire"] >= 50000:
            score += config.salaire_50k

        else:
            score += config.salaire_min

        # marié
        if data["marie"] == "oui":
            score += config.marie

        # enfants
        if data["enfants"] <= 2:
            score += config.enfants

        # contrat
        if data["type_contrat"] == "cdi":
            score += config.cdi

        elif data["type_contrat"] == "fonctionnaire":
            score += config.fonctionnaire

        # ancienneté
        if data["anciennete"] >= 5:
            score += config.anciennete

        # apport
        if data["apport"] >= 500000:
            score += config.apport

        taux_endettement = (
            data["charges"] / data["salaire"]
        ) * 100

        if taux_endettement < 35:
            score += config.taux_endettement

        decision = "ACCEPTE"

        if score < 50:
            decision = "REFUSE"

        return Response({
            "score": score,
            "decision": decision,
            "taux_endettement": round(
                taux_endettement,
                2
            )
        })
    