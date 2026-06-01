from rest_framework import serializers
from .models import Simulation

class SimulationInputSerializer(serializers.Serializer):
    client_id = serializers.IntegerField()
    prix_bien = serializers.FloatField()
    apport = serializers.FloatField()
    marge = serializers.FloatField()
    duree_mois = serializers.IntegerField()


class SimulationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Simulation
        fields = '__all__'