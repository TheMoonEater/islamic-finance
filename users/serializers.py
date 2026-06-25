from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer
)


User = get_user_model()


class RegisterSerializer(
    serializers.ModelSerializer
):

    password = serializers.CharField(
        write_only=True
    )

    class Meta:
        model = User

        fields = (
            "id",
            "username",
            "email",
            "password",
            "phone",
            "nom",
            "prenom",
            "date_naissance",
            "numero_cni",
        )

    def create(self, validated_data):

        user = User.objects.create_user(

            username=validated_data["username"],

            email=validated_data["email"],

            password=validated_data["password"],

            phone=validated_data.get(
                "phone",
                ""
            ),

            nom=validated_data.get(
                "nom",
                ""
            ),

            prenom=validated_data.get(
                "prenom",
                ""
            ),

            date_naissance=validated_data.get(
                "date_naissance"
            ),

            numero_cni=validated_data.get(
                "numero_cni",
                ""
            ),

            role="CLIENT"
        )

        return user
    


class CustomTokenObtainPairSerializer(
    TokenObtainPairSerializer
):

    @classmethod
    def get_token(cls, user):

        token = super().get_token(user)

        token["role"] = user.role

        return token

    def validate(self, attrs):

        data = super().validate(attrs)

        data["role"] = self.user.role

        return data