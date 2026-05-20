from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from clients.models import Client
from users.permissions import CanManageScoring
from .models import Scoring
from .serializers import ScoringSerializer

from .serializers import (
    ScoringSerializer,
    ClientScoringSerializer
)

from .services import (
    calcul_score,
    get_decision
)


class CalculateScoringView(APIView):
    permission_classes = [
        CanManageScoring
    ]

    def post(self, request):
        client_id = request.data.get("client_id")

        try:
            client = Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            return Response(
                {"error": "Client introuvable"},
                status=status.HTTP_404_NOT_FOUND
            )

        score, taux = calcul_score(client)
        decision = get_decision(score)

        scoring = Scoring.objects.create(
            client=client,
            score=score,
            taux_endettement=taux,
            decision=decision
        )

        if request.user.role == 'CLIENT':
            serializer = ClientScoringSerializer(scoring)
        else:
            serializer = ScoringSerializer(scoring)

        return Response(serializer.data)
