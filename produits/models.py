from django.db import models


class Produit(models.Model):

    nom = models.CharField(max_length=255)

    description = models.TextField()

    prix = models.FloatField()

    image = models.URLField(blank=True)

    stock = models.IntegerField(default=1)

    def __str__(self):
        return self.nom