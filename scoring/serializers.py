from rest_framework import serializers
from .models import Scoring


class ScoringSerializer(serializers.ModelSerializer):

    class Meta:
        model = Scoring
        fields = '__all__'