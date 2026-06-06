from django.contrib import admin
from .models import Produit, Category

admin.site.register(Category)
admin.site.register(Produit)