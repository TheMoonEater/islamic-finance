from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    ROLE_CHOICES = (
        ('CLIENT', 'Client'),
        ('EMPLOYE', 'Employe'),
        ('RETAIL', 'Retail'),
        ('ADMIN', 'Admin'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='CLIENT'
    )

    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.username