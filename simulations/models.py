from django.db import models
from clients.models import Client


class Simulation(models.Model):

    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE
    )

    prix_bien = models.FloatField()

    salaire_acheteur = models.FloatField(default=0)

    salaire_co_acheteur = models.FloatField(
        default=0,
        blank=True
    )

    salaire_total = models.FloatField(default=0)

    ce_brute = models.FloatField(default=0)

    credit_consomme = models.FloatField(default=0)

    ce_nette = models.FloatField(default=0)

    apport = models.FloatField(default=0)

    montant_finance = models.FloatField()

    marge = models.FloatField()

    prix_final = models.FloatField()

    duree_mois = models.IntegerField()

    mensualite = models.FloatField()

    montant_remboursement = models.FloatField(
        default=0
    )

    montant_total_marge = models.FloatField(
        default=0
    )

    montant_total_tva = models.FloatField(
        default=0
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Simulation {self.id}"