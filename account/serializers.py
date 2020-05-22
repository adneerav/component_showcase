from rest_framework import serializers

from account.models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "full_name", "email", "username", "password",
            "active", "staff", "admin"
        )

    def create(self, validated_data):
        password = validated_data.pop("password")
        if not password:
            raise ValueError("Password required.")
        user = User.objects.create_user(
            email=validated_data.pop("email"),
            username=validated_data.pop("username"),
            password=password,
            full_name=validated_data.pop("full_name"),
            active=validated_data.pop("active"),
            admin=validated_data.pop("admin"),
            staff=validated_data.pop("staff"),
        )
        return user
