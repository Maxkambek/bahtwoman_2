from rest_framework import serializers
from .models import User, phone_regex, UserCard


class UserCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCard
        fields = ['user', 'number', 'expire_date', 'holder']


class VerifyPhoneSerializer(serializers.Serializer):
    phone = serializers.CharField(validators=[phone_regex], max_length=12)
    code = serializers.IntegerField(max_value=99999)


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone', 'name', 'password']

    password = serializers.CharField(max_length=64, min_length=4, write_only=True)
    phone = serializers.CharField(max_length=12, validators=[phone_regex])

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone', 'password']

    phone = serializers.CharField(validators=[phone_regex])
    password = serializers.CharField(write_only=True)


class ResetPasswordSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=12, validators=[phone_regex])


class ResetPasswordConfirmSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=12, validators=[phone_regex])
    password = serializers.CharField(max_length=64)


class ChangePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['password']

    password = serializers.CharField(max_length=64, write_only=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'phone', 'name', 'email']

    phone = serializers.CharField(max_length=12, validators=[phone_regex])
    id = serializers.IntegerField(read_only=True)