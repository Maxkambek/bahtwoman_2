from rest_framework import serializers
from .models import User, phone_regex, UserCard, UserDetails, Region, District


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name']


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['id', 'region', 'name']


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        exclude = ['user']


class UserCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCard
        fields = ['user', 'number', 'expire_date', 'holder']


class VerifyPhoneSerializer(serializers.Serializer):
    phone = serializers.CharField(validators=[phone_regex], max_length=12)
    code = serializers.IntegerField(max_value=9999)
    # name = serializers.CharField(max_length=350)
    # last_name = serializers.CharField(max_length=132)
    # given_name = serializers.CharField(max_length=132)
    # date_birth = serializers.CharField(max_length=132)
    # passport_num = serializers.CharField(max_length=20)
    # passport_expire = serializers.CharField(max_length=20)
    # district = serializers.IntegerField()
    # address = serializers.CharField(max_length=223)
    password = serializers.CharField(max_length=64, min_length=4, write_only=True)


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone']

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
        fields = ['password', 'old_password']

    password = serializers.CharField(max_length=64, write_only=True)
    old_password = serializers.CharField(max_length=64, write_only=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'phone', 'name', 'last_name', 'given_name', 'date_birth', 'passport_num', 'passport_expire',
                  'district', 'address']

    phone = serializers.CharField(max_length=12, validators=[phone_regex])
    id = serializers.IntegerField(read_only=True)
