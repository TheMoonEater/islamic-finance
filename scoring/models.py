from django.db import models
from clients.models import Client


class Scoring(models.Model):

    DECISION_CHOICES = (
        ('ELIGIBLE', 'Eligible'),
        ('A_ANALYSER', 'A analyser'),
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