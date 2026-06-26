from rest_framework import serializers


class ScoringSerializer(serializers.Serializer):

    # Identification
    age = serializers.IntegerField()

    nombre_personnes_charge = serializers.IntegerField()

    habitation = serializers.CharField()

    niveau_instruction = serializers.CharField()

    # Professionnel
    secteur_activite = serializers.CharField()

    anciennete = serializers.IntegerField()

    type_contrat = serializers.CharField()

    # Financier
    salaire = serializers.FloatField()

    autres_revenus = serializers.FloatField()

    charges = serializers.FloatField()