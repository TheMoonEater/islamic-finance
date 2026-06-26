from rest_framework import generics
from rest_framework.response import Response

from scoring_config.models import ScoringConfig
from .serializers import ScoringSerializer


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

        score = 0

        # =========================
        # AGE
        # =========================

        age = float(
            request.data.get("age", 0)
        )

        if age < 30:
            score += config.age_jeune

        elif age <= 50:
            score += config.age_moyen

        else:
            score += config.age_senior

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
            score += config.personnes_charge

        # =========================
        # HABITATION
        # =========================

        habitation = request.data.get(
            "habitation",
            ""
        )

        if habitation == "Proprietaire":
            score += config.habitation_proprietaire

        elif habitation == "Locataire":
            score += config.habitation_locataire

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
            score += config.niveau_universitaire

        elif niveau == "Secondaire":
            score += config.niveau_secondaire

        # =========================
        # SECTEUR ACTIVITE
        # =========================

        secteur = request.data.get(
            "secteur_activite",
            ""
        )

        if secteur == "PUBLIC":
            score += config.secteur_public

        elif secteur == "PRIVE":
            score += config.secteur_prive

        # =========================
        # CONTRAT
        # =========================

        contrat = (
            data["type_contrat"]
            .lower()
        )

        if contrat == "cdi":
            score += config.cdi

        elif contrat == "fonctionnaire":
            score += config.fonctionnaire

        elif contrat == "cdd":
            score += config.cdd

        # =========================
        # ANCIENNETE
        # =========================

        if data["anciennete"] >= 5:
            score += config.anciennete

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
            score += config.salaire_100k

        elif salaire >= 50000:
            score += config.salaire_50k

        else:
            score += config.salaire_min

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
            score += config.autres_revenus

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
            score += config.endettement

        # =========================
        # DECISION
        # =========================

        decision = "REFUSE"

        if (
            score >=
            config.seuil_acceptation
        ):
            decision = "ACCEPTE"

        return Response({
            "score": score,
            "decision": decision,
            "taux_endettement": round(
                taux_endettement,
                2
            )
        })