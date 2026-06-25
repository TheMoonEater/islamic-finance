from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    ROLE_CHOICES = (

        ('CLIENT', 'Client'),
        ('EMPLOYE', 'Employe'),
        ('RETAIL', 'Retail'),
        ('COMITE', 'Comite'),
        ('ADMIN', 'Admin'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='CLIENT'
    )

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    nom = models.CharField(
        max_length=100,
        blank=True
    )

    prenom = models.CharField(
        max_length=100,
        blank=True
    )

    date_naissance = models.DateField(
        null=True,
        blank=True
    )

    numero_cni = models.CharField(
        max_length=50,
        blank=True
    )

    def __str__(self):
        return self.username