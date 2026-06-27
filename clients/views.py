from io import BytesIO

from django.http import HttpResponse

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Client
from .serializers import ClientSerializer

from scoring.models import Scoring
from documents.models import Document


class ClientViewSet(viewsets.ModelViewSet):

    queryset = Client.objects.all()

    serializer_class = ClientSerializer

    permission_classes = [
        IsAuthenticated
    ]

    # =========================
    # MON PROFIL
    # =========================

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

        if request.method == "GET":

            serializer = ClientSerializer(
                client
            )

            return Response(
                serializer.data
            )

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
    # DOSSIER CLIENT
    # =========================

    @action(
        detail=True,
        methods=["get"]
    )
    def dossier(self, request, pk=None):

        client = self.get_object()

        dernier_scoring = (
            Scoring.objects
            .filter(client=client)
            .order_by("-created_at")
            .first()
        )

        historiques = (
            Scoring.objects
            .filter(client=client)
            .order_by("-created_at")
        )

        documents = Document.objects.filter(
            user=client.user
        )

        return Response({

            "client":
            ClientSerializer(client).data,

            "dernier_scoring":
            {
                "id":
                dernier_scoring.id,

                "score":
                dernier_scoring.score,

                "decision":
                dernier_scoring.decision,

                "taux_endettement":
                dernier_scoring.taux_endettement,

                "date":
                dernier_scoring.created_at

            } if dernier_scoring else None,

            "historique_scoring": [

                {
                    "id": s.id,

                    "score": s.score,

                    "decision": s.decision,

                    "date": s.created_at
                }

                for s in historiques

            ],

            "documents": [

                {
                    "id": d.id,

                    "type_document":
                    d.type_document,

                    "fichier":
                    d.fichier.url,

                    "valide":
                    d.valide,

                    "date":
                    d.created_at
                }

                for d in documents

            ]
        })

    # =========================
    # PDF DOSSIER CLIENT
    # =========================

    @action(
        detail=True,
        methods=["get"]
    )
    def pdf(self, request, pk=None):

        client = self.get_object()

        dernier_scoring = (
            Scoring.objects
            .filter(client=client)
            .order_by("-created_at")
            .first()
        )

        historiques = (
            Scoring.objects
            .filter(client=client)
            .order_by("-created_at")
        )

        documents = Document.objects.filter(
            user=client.user
        )

        buffer = BytesIO()

        doc = SimpleDocTemplate(buffer)

        styles = getSampleStyleSheet()

        elements = []

        # =====================
        # TITRE
        # =====================

        elements.append(
            Paragraph(
                "DOSSIER CLIENT COMPLET",
                styles["Title"]
            )
        )

        elements.append(
            Spacer(1, 20)
        )

        # =====================
        # IDENTITE
        # =====================

        elements.append(
            Paragraph(
                "IDENTIFICATION",
                styles["Heading2"]
            )
        )

        elements.append(
            Paragraph(
                f"Nom : {client.nom}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Prénom : {client.prenom}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Date naissance : {client.date_naissance}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Situation familiale : {client.situation_familiale}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Email : {client.email}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Téléphone : {client.telephone}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Adresse : {client.adresse}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Personnes à charge : {client.nombre_personnes_charge}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Habitation : {client.habitation}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Niveau instruction : {client.niveau_instruction}",
                styles["Normal"]
            )
        )

        elements.append(
            Spacer(1, 20)
        )

        # =====================
        # PROFESSION
        # =====================

        elements.append(
            Paragraph(
                "SITUATION PROFESSIONNELLE",
                styles["Heading2"]
            )
        )

        elements.append(
            Paragraph(
                f"Secteur activité : {client.secteur_activite}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Contrat : {client.type_contrat}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Ancienneté : {client.anciennete_annees} ans",
                styles["Normal"]
            )
        )

        elements.append(
            Spacer(1, 20)
        )

        # =====================
        # FINANCE
        # =====================

        elements.append(
            Paragraph(
                "SITUATION FINANCIERE",
                styles["Heading2"]
            )
        )

        elements.append(
            Paragraph(
                f"Salaire : {client.salaire_mensuel} DA",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Autres revenus : {client.autres_revenus} DA",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Charges : {client.charges_mensuelles} DA",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Crédits en cours : {client.credits_en_cours} DA",
                styles["Normal"]
            )
        )

        elements.append(
            Spacer(1, 20)
        )

        # =====================
        # SCORING
        # =====================

        if dernier_scoring:

            elements.append(
                Paragraph(
                    "DERNIER SCORING",
                    styles["Heading2"]
                )
            )

            elements.append(
                Paragraph(
                    f"Score : {dernier_scoring.score}",
                    styles["Normal"]
                )
            )

            elements.append(
                Paragraph(
                    f"Décision : {dernier_scoring.decision}",
                    styles["Normal"]
                )
            )

            elements.append(
                Paragraph(
                    f"Taux endettement : {dernier_scoring.taux_endettement} %",
                    styles["Normal"]
                )
            )

            elements.append(
                Spacer(1, 20)
            )

        # =====================
        # HISTORIQUE
        # =====================

        elements.append(
            Paragraph(
                "HISTORIQUE SCORING",
                styles["Heading2"]
            )
        )

        for score in historiques:

            elements.append(
                Paragraph(
                    f"{score.created_at.strftime('%d/%m/%Y')} - "
                    f"Score {score.score} - "
                    f"{score.decision}",
                    styles["Normal"]
                )
            )

        elements.append(
            Spacer(1, 20)
        )

        # =====================
        # DOCUMENTS
        # =====================

        elements.append(
            Paragraph(
                "DOCUMENTS DEPOSES",
                styles["Heading2"]
            )
        )

        if documents.exists():

            for document in documents:

                statut = (
                    "Validé"
                    if document.valide
                    else "En attente"
                )

                elements.append(
                    Paragraph(
                        f"{document.type_document} - {statut}",
                        styles["Normal"]
                    )
                )

        else:

            elements.append(
                Paragraph(
                    "Aucun document",
                    styles["Normal"]
                )
            )

        doc.build(elements)

        pdf = buffer.getvalue()

        buffer.close()

        response = HttpResponse(
            pdf,
            content_type="application/pdf"
        )

        filename = (
            f"Dossier_"
            f"{client.nom}_"
            f"{client.prenom}.pdf"
        )

        response[
            "Content-Disposition"
        ] = (
            f'attachment; filename="{filename}"'
        )

        return response


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

            "user_id":
            request.user.id,

            "username":
            request.user.username,

            "role":
            request.user.role

        })