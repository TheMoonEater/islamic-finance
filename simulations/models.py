from django.db import models
from clients.models import Client


class Simulation(models.Model):

    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE
    )

    prix_bien = models.FloatField()

    apport = models.FloatField(default=0)

    montant_finance = models.FloatField()

    marge = models.FloatField()

    prix_final = models.FloatField()

    duree_mois = models.IntegerField()

    mensualite = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Simulation {self.id}"