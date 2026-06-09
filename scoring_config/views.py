from rest_framework.views import APIView
from rest_framework.response import Response

from .models import ScoringConfig
from .serializers import (
    ScoringConfigSerializer
)


class ScoringConfigView(APIView):

    def get(self, request):

        config = (
            ScoringConfig.objects.first()
        )

        serializer = (
            ScoringConfigSerializer(config)
        )

        return Response(
            serializer.data
        )

    def put(self, request):

        config = (
            ScoringConfig.objects.first()
        )

        serializer = (
            ScoringConfigSerializer(
                config,
                data=request.data
            )
        )

        serializer.is_valid(
            raise_exception=True
        )

        serializer.save()

        return Response(
            serializer.data
        )