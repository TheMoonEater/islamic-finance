from rest_framework import serializers


class ScoringSerializer(serializers.Serializer):

    salaire = serializers.FloatField()

    charges = serializers.FloatField()

    marie = serializers.ChoiceField(
        choices=[
            ("oui", "Oui"),
            ("non", "Non")
        ]
    )

    enfants = serializers.IntegerField()

    type_contrat = serializers.ChoiceField(
        choices=[
            ("cdi", "CDI"),
            ("cdd", "CDD"),
            ("fonctionnaire", "Fonctionnaire")
        ]
    )

    anciennete = serializers.IntegerField()

    apport = serializers.FloatField()