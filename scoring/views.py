from rest_framework import generics
from rest_framework.response import Response

from scoring_config.models import ScoringConfig
from .serializers import ScoringSerializer

from clients.models import Client
from scoring.models import Scoring


class CalculateScoringView(generics.GenericAPIView):

    serializer_class = ScoringSerializer

    def post(self, request):

        serializer = self.get_serializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        data = serializer.validated_data

        config = ScoringConfig.objects.first()

        if not config:
            config = ScoringConfig.objects.create()

        identification = 0
        professionnel = 0
        financier = 0

        # =========================
        # AGE
        # =========================

        age = float(
            request.data.get("age", 0)
        )

        if age < 30:
            identification += config.age_jeune

        elif age <= 50:
            identification += config.age_moyen

        else:
            identification += config.age_senior

        # =========================
        # PERSONNES A CHARGE
        # =========================

        personnes_charge = int(
            request.data.get(
                "nombre_personnes_charge",
                0
            )
        )

        if personnes_charge <= 2:
            identification += config.personnes_charge

        # =========================
        # HABITATION
        # =========================

        habitation = request.data.get(
            "habitation",
            ""
        )

        if habitation == "Proprietaire":
            identification += config.habitation_proprietaire

        elif habitation == "Locataire":
            identification += config.habitation_locataire

        # =========================
        # NIVEAU INSTRUCTION
        # =========================

        niveau = request.data.get(
            "niveau_instruction",
            ""
        )

        if niveau in [
            "Universitaire",
            "Master",
            "Doctorat"
        ]:
            identification += config.niveau_universitaire

        elif niveau == "Secondaire":
            identification += config.niveau_secondaire

        # =========================
        # SECTEUR ACTIVITE
        # =========================

        secteur = request.data.get(
            "secteur_activite",
            ""
        )

        if secteur == "PUBLIC":
            professionnel += config.secteur_public

        elif secteur == "PRIVE":
            professionnel += config.secteur_prive

        # =========================
        # CONTRAT
        # =========================

        contrat = (
            data["type_contrat"]
            .lower()
        )

        if contrat == "cdi":
            professionnel += config.cdi

        elif contrat == "fonctionnaire":
            professionnel += config.fonctionnaire

        elif contrat == "cdd":
            professionnel += config.cdd

        # =========================
        # ANCIENNETE
        # =========================

        if data["anciennete"] >= 5:
            professionnel += config.anciennete

        # =========================
        # SALAIRE
        # =========================

        salaire = (
            data["salaire"]
            +
            float(
                request.data.get(
                    "autres_revenus",
                    0
                )
            )
        )

        if salaire >= 100000:
            financier += config.salaire_100k

        elif salaire >= 50000:
            financier += config.salaire_50k

        else:
            financier += config.salaire_min

        # =========================
        # AUTRES REVENUS
        # =========================

        autres_revenus = float(
            request.data.get(
                "autres_revenus",
                0
            )
        )

        if autres_revenus > 0:
            financier += config.autres_revenus

        # =========================
        # TAUX ENDETTEMENT
        # =========================

        taux_endettement = 0

        if salaire > 0:

            taux_endettement = (
                data["charges"]
                / salaire
            ) * 100

        if taux_endettement < 35:
            financier += config.endettement

        # =========================
        # DECISION
        # =========================

        score = round(
            (
                identification
                + professionnel
                + financier
            ) / 3,
            2
        )

        decision = "REFUSE"

        if (
            score >=
            config.seuil_acceptation
        ):
            decision = "ACCEPTE"

        # =========================
        # ENREGISTREMENT SCORING
        # =========================

        client_id = request.data.get(
            "client_id"
        )

        if client_id:

            client = Client.objects.get(
                id=client_id
            )

            scoring = Scoring.objects.create(
                client=client,
                score=score,
                taux_endettement=taux_endettement,
                decision=decision
            )

        else:

            scoring = None

        return Response({

            "score": score,

            "decision": decision,

            "taux_endettement": round(
                taux_endettement,
                2
            ),

            "scoring_id":
            scoring.id if scoring else None
        })