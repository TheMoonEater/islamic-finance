from rest_framework import serializers

from .models import ScoringConfig


class ScoringConfigSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = ScoringConfig
        fields = "__all__"