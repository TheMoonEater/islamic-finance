from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .serializers import ScoringSerializer


class CalculateScoringView(generics.GenericAPIView):

    serializer_class = ScoringSerializer

    def post(self, request):

        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        score = 0

        # salaire
        if data["salaire"] >= 100000:
            score += 30
        elif data["salaire"] >= 50000:
            score += 20
        else:
            score += 10

        # marié
        if data["marie"] == "oui":
            score += 10

        # enfants
        if data["enfants"] <= 2:
            score += 10

        # contrat
        if data["type_contrat"] == "cdi":
            score += 25

        elif data["type_contrat"] == "fonctionnaire":
            score += 30

        # ancienneté
        if data["anciennete"] >= 5:
            score += 15

        # apport
        if data["apport"] >= 500000:
            score += 20

        taux_endettement = (
            data["charges"] / data["salaire"]
        ) * 100

        if taux_endettement < 35:
            score += 20

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