from django.db import models
from users.models import User


class Document(models.Model):

    TYPE_CHOICES = (

        ("CNI", "Carte d'identité"),

        ("PAIE", "Fiche de paie"),

        ("TRAVAIL", "Attestation de travail"),

        ("JUSTIFICATIF", "Justificatif"),

        ("AUTRE", "Autre"),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    type_document = models.CharField(
        max_length=30,
        choices=TYPE_CHOICES
    )

    fichier = models.FileField(
        upload_to="documents/"
    )

    valide = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return (
            f"{self.user.username} - "
            f"{self.type_document}"
        )