from django.db import models

from clients.models import Client
from scoring.models import Scoring
from simulations.models import Simulation


class DemandeFinancement(models.Model):

    STATUS_CHOICES = (
        ('BROUILLON', 'Brouillon'),
        ('EN_ANALYSE', 'En analyse'),
        ('VALIDATION_EMPLOYE', 'Validation employe'),
        ('VALIDATION_RETAIL', 'Validation retail'),
        ('COMITE', 'Comite'),
        ('ACCEPTE', 'Accepte'),
        ('REFUSE', 'Refuse'),
    )

    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE
    )

    scoring = models.OneToOneField(
        Scoring,
        on_delete=models.CASCADE
    )

    simulation = models.OneToOneField(
        Simulation,
        on_delete=models.CASCADE
    )

    statut = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='BROUILLON'
    )

    commentaire = models.TextField(blank=True)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"Demande {self.id}"


class WorkflowHistory(models.Model):

    demande = models.ForeignKey(
        DemandeFinancement,
        on_delete=models.CASCADE
    )

    ancien_statut = models.CharField(
        max_length=30
    )

    nouveau_statut = models.CharField(
        max_length=30
    )

    commentaire = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.demande.id}"