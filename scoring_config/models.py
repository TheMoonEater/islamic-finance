from django.db import models


class ScoringConfig(models.Model):

    # Identification

    age_jeune = models.IntegerField(default=10)

    age_moyen = models.IntegerField(default=15)

    age_senior = models.IntegerField(default=20)

    personnes_charge = models.IntegerField(default=10)

    habitation_proprietaire = models.IntegerField(default=20)

    habitation_locataire = models.IntegerField(default=10)

    niveau_universitaire = models.IntegerField(default=20)

    niveau_secondaire = models.IntegerField(default=10)

    # Professionnel

    secteur_public = models.IntegerField(default=20)

    secteur_prive = models.IntegerField(default=10)

    cdi = models.IntegerField(default=25)

    fonctionnaire = models.IntegerField(default=30)

    cdd = models.IntegerField(default=10)

    anciennete = models.IntegerField(default=20)

    # Financier

    salaire_100k = models.IntegerField(default=30)

    salaire_50k = models.IntegerField(default=20)

    salaire_min = models.IntegerField(default=10)

    autres_revenus = models.IntegerField(default=10)

    endettement = models.IntegerField(default=20)

    seuil_acceptation = models.IntegerField(default=70)

    def __str__(self):
        return "Configuration Scoring"