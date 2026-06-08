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
        )

    def create(self, validated_data):

        user = User.objects.create_user(

            username=validated_data["username"],

            email=validated_data.get(
                "email",
                ""
            ),

            password=validated_data["password"],

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