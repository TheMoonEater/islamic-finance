from django.db import models



class Category(models.Model):

    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom



class Produit(models.Model):

    CATEGORY_CHOICES = (
    ("VOITURE", "Voiture"),
    ("MOTO", "Moto"),
    ("ELECTROMENAGER", "Électroménager"),
    )

    nom = models.CharField(max_length=255)

    description = models.TextField()

    prix = models.FloatField()

    image = models.URLField(blank=True)

    stock = models.IntegerField(default=1)

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default="VOITURE"
    )

    def __str__(self):
        return self.nom