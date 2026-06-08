from django.db import models


class ScoringConfig(models.Model):

    salaire_100k = models.IntegerField(
        default=30
    )

    salaire_50k = models.IntegerField(
        default=20
    )

    salaire_min = models.IntegerField(
        default=10
    )

    mariage = models.IntegerField(
        default=10
    )

    enfants = models.IntegerField(
        default=10
    )

    cdi = models.IntegerField(
        default=25
    )

    fonctionnaire = models.IntegerField(
        default=30
    )

    anciennete = models.IntegerField(
        default=15
    )

    apport = models.IntegerField(
        default=20
    )

    endettement = models.IntegerField(
        default=20
    )

    seuil_acceptation = models.IntegerField(
        default=50
    )

    def __str__(self):
        return "Configuration scoring"