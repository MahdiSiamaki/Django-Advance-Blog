from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from ...models import User

class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True,max_length=100,min_length=4)
    class Meta:
        model = User
        fields = ['email','password', 'password1']

    def validate(self, attrs):
        if attrs['password'] != attrs['password1']:
            raise serializers.ValidationError("Password did not match")
        try:
            validate_password(attrs['password'])
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({'password': list(e.messages)})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password1')
        return User.objects.create_user(**validated_data)