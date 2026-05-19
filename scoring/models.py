from django.db import models
from clients.models import Client


class Scoring(models.Model):

    DECISION_CHOICES = (
        ('ELIGIBLE', 'Eligible'),
        ('REFUSE', 'Refuse'),
    )

    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    score = models.FloatField()

    taux_endettement = models.FloatField()

    decision = models.CharField(
        max_length=20,
        choices=DECISION_CHOICES
    )

    commentaire = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client} - {self.score}"
    




class ScoringRule(models.Model):

    RULE_TYPES = (
        ('SALAIRE', 'Salaire'),
        ('ANCIENNETE', 'Anciennete'),
        ('CONTRAT', 'Contrat'),
        ('ENDETTEMENT', 'Endettement'),
        ('SITUATION', 'Situation'),
    )

    nom = models.CharField(
        max_length=100
    )

    type_regle = models.CharField(
        max_length=30,
        choices=RULE_TYPES
    )

    valeur = models.CharField(
        max_length=100
    )

    points = models.IntegerField()

    actif = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.nom