from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from django.utils.translation import gettext_lazy as _
from ...models import User, Profile

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(
        write_only=True, max_length=100, min_length=4
    )

    class Meta:
        model = User
        fields = ["email", "password", "password1"]

    def validate(self, attrs):
        if attrs["password"] != attrs["password1"]:
            raise serializers.ValidationError("Password did not match")
        try:
            validate_password(attrs["password"])
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"password": list(e.messages)})
        return attrs

    def create(self, validated_data):
        validated_data.pop("password1")
        return User.objects.create_user(**validated_data)


class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(label=_("Email"), write_only=True)
    password = serializers.CharField(
        label=_("Password"),
        style={"input_type": "password"},
        trim_whitespace=False,
        write_only=True,
    )
    token = serializers.CharField(label=_("Token"), read_only=True)

    def validate(self, attrs):
        username = attrs.get("email")
        password = attrs.get("password")

        if username and password:
            user = authenticate(
                request=self.context.get("request"),
                username=username,
                password=password,
            )

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _("Unable to log in with provided credentials.")
                raise serializers.ValidationError(msg, code="authorization")
            if not user.is_verified:
                msg = _("User account is disabled.")
                raise serializers.ValidationError(msg, code="authorization")
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code="authorization")

        attrs["user"] = user
        return attrs


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        if not self.user.is_verified:
            msg = _("User account is disabled.")
            raise serializers.ValidationError(msg, code="authorization")
        # Add custom claims
        data["email"] = self.user.email
        data["user_id"] = self.user.id
        return data


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_password1 = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs["new_password"] != attrs["new_password1"]:
            raise serializers.ValidationError("Password did not match")
        try:
            validate_password(attrs["new_password"])
        except exceptions.ValidationError as e:
            raise serializers.ValidationError(
                {"new_password": list(e.messages)}
            )
        return attrs


class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source="user.email", read_only=True)

    class Meta:
        model = Profile
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "image",
            "description",
        ]


class EmailVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()
