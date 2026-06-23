from rest_framework import serializers
from .models import Simulation

class SimulationInputSerializer(serializers.Serializer):
    client_id = serializers.IntegerField()
    prix_bien = serializers.FloatField()
    apport = serializers.FloatField()
    marge = serializers.FloatField()

    salaire_acheteur = serializers.FloatField()

    salaire_co_acheteur = serializers.FloatField(
        required=False,
        default=0
    )

    credit_consomme = serializers.FloatField(
        default=0
    )
    
    duree_mois = serializers.IntegerField()


class SimulationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Simulation
        fields = '__all__'