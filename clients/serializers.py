from rest_framework import serializers
from datetime import date

from .models import Client


class ClientSerializer(serializers.ModelSerializer):

    age = serializers.SerializerMethodField()

    class Meta:
        model = Client

        fields = "__all__"

    def get_age(self, obj):

        today = date.today()

        return (
            today.year
            - obj.date_naissance.year
            - (
                (
                    today.month,
                    today.day
                )
                <
                (
                    obj.date_naissance.month,
                    obj.date_naissance.day
                )
            )
        )