from rest_framework import viewsets

from .models import Produit
from .serializers import ProduitSerializer


class ProduitViewSet(viewsets.ModelViewSet):

    queryset = Produit.objects.all()

    serializer_class = ProduitSerializer


    def list(self, request):

        print("NB PRODUITS =", Produit.objects.count())

        return super().list(request)