from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

# Always use get_user_model() so it points to your CustomUser
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "bio", "profile_picture", "followers"]


class RegisterSerializer(serializers.ModelSerializer):
    # ✅ Explicit CharField for password
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        # ✅ Use create_user() (best practice)
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["password"]
        )
        # ✅ Create token for authentication
        Token.objects.create(user=user)
        return user


