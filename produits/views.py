from rest_framework import viewsets

from .models import Produit
from .serializers import ProduitSerializer


class ProduitViewSet(viewsets.ModelViewSet):

    queryset = Produit.objects.all()

    serializer_class = ProduitSerializer

    def get_queryset(self):

        queryset = Produit.objects.all()

        search = self.request.GET.get("search")
        category = self.request.GET.get("category")
        ordering = self.request.GET.get("ordering")

        if search:
            queryset = queryset.filter(
                nom__icontains=search
            )

        if category:
            queryset = queryset.filter(
                category=category
            )

        if ordering:
            queryset = queryset.order_by(
                ordering
            )

        return queryset