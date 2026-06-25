from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Client
from .serializers import ClientSerializer


class ClientViewSet(viewsets.ModelViewSet):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    permission_classes = [
        IsAuthenticated
    ]

    @action(
        detail=False,
        methods=["get", "patch"]
    )
    def me(self, request):

        try:

            client = Client.objects.get(
                user=request.user
            )

        except Client.DoesNotExist:

            return Response(
                {
                    "error":
                    "Profil client introuvable"
                },
                status=404
            )

        # GET
        if request.method == "GET":

            serializer = ClientSerializer(
                client
            )

            return Response(
                serializer.data
            )

        # PATCH
        serializer = ClientSerializer(
            client,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data
            )

        return Response(
            serializer.errors,
            status=400
        )


# =========================
# DEBUG AUTH
# =========================

class DebugAuthView(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request):

        return Response({
            "authorization":
            request.META.get(
                "HTTP_AUTHORIZATION"
            )
        })


# =========================
# DEBUG JWT
# =========================

class DebugJWTView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        return Response({
            "user_id": request.user.id,
            "username": request.user.username,
            "role": request.user.role
        })