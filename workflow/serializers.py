from rest_framework import serializers

from .models import (
    DemandeFinancement,
    WorkflowHistory
)


class DemandeSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = DemandeFinancement
        fields = '__all__'


class WorkflowHistorySerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = WorkflowHistory
        fields = '__all__'