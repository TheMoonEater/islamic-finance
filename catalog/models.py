from django.db import models


class Category(models.Model):

    nom = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.nom


class Product(models.Model):

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    nom = models.CharField(
        max_length=200
    )

    description = models.TextField()

    prix = models.FloatField()

    stock = models.IntegerField()

    image = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True
    )

    disponible_financement = models.BooleanField(
        default=True
    )

    actif = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.nom