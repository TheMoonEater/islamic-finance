from django.db import models
from users.models import User


class Client(models.Model):

    SITUATION_CHOICES = (
        ('CELIBATAIRE', 'Celibataire'),
        ('MARIE', 'Marie'),
        ('DIVORCE', 'Divorce'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)

# Identification

    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)

    date_naissance = models.DateField()

    situation_familiale = models.CharField(
        max_length=20,
        choices=SITUATION_CHOICES
    )

    adresse = models.TextField()
    telephone = models.CharField(max_length=20)
    email = models.EmailField()

    nombre_personnes_charge = models.IntegerField(
        default=0
    )

    habitation = models.CharField(
        max_length=100,
        blank=True
    )

    niveau_instruction = models.CharField(
        max_length=100,
        blank=True
    )

    # professionnel
    type_contrat = models.CharField(max_length=50)
    salaire_mensuel = models.FloatField()
    anciennete_annees = models.IntegerField()
    secteur_activite = models.CharField(
        max_length=20,
        blank=True
    )

    # finance
    charges_mensuelles = models.FloatField(default=0)
    credits_en_cours = models.FloatField(default=0)
    autres_revenus = models.FloatField(
        default=0
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"