from django.db import models

from users.models import User
from cart.models import Cart


class Order(models.Model):

    STATUS_CHOICES = (

        ('PENDING', 'Pending'),

        ('SCORING', 'Scoring'),

        ('ANALYSIS', 'Analysis'),

        ('APPROVED', 'Approved'),

        ('REJECTED', 'Rejected'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE
    )

    total = models.FloatField()

    statut = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Commande {self.id}"