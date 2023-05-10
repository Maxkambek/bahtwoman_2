from random import randint
from django.contrib.auth import authenticate
from rest_framework import generics, status, permissions, response, views
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from .utils import verify
from .serializers import RegisterSerializer, LoginSerializer, ChangePasswordSerializer, ResetPasswordSerializer, \
    UserSerializer, VerifyPhoneSerializer, ResetPasswordConfirmSerializer, UserCardSerializer, UserDetailsSerializer
from .models import User, VerifyPhone, UserCard, UserDetails, District
from .validators import expire_date_validator, card_number_validator


class UserDetailsCreateAPIView(generics.CreateAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['user'] = self.request.user
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()


class UserCardAPI(generics.CreateAPIView):
    queryset = UserCard.objects.all()
    serializer_class = UserCardSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, *args, **kwargs):
        qs = self.queryset.filter(user_id=self.request.user.id).all()
        serializer = self.get_serializer(qs, many=True)
        return response.Response(serializer.data)

    def post(self, request, *args, **kwargs):
        num = self.request.data['number']
        mud = self.request.data['expire_date']
        if card_number_validator(num) is False:
            return response.Response({'success': False,
                                      'message': "Karta raqami noto'g'ri kiritildi\nIltimos faqat Uzcard yoki Humo kartalarini kiriting!"},
                                     status=status.HTTP_400_BAD_REQUEST)
        if expire_date_validator(mud) is False:
            return response.Response(
                {'success': False,
                 'message': "Kartani amal qilish muddati noto'g'ri kiritildi!\n 05/27 shunaqa tarzda kiritilsin!"},
                status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response({'success': True})


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        phone = self.request.data['phone']
        if User.objects.filter(phone=phone, is_active=True).first():
            return response.Response({'message': "This number already exist"}, status=status.HTTP_302_FOUND)
        code = str(randint(1000, 10000))
        verify(phone, code)
        VerifyPhone.objects.create(phone=phone, code=code)
        return response.Response({"success": True, 'message': "A confirmation code was sent to the phone number!!!"},
                                 status=status.HTTP_200_OK)


class RegisterConfirmAPI(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = VerifyPhoneSerializer

    def post(self, request, *args, **kwargs):
        phone = self.request.data['phone']
        password = self.request.data['password']
        code = self.request.data['code']
        name = self.request.data['name']
        last_name = self.request.data['last_name']
        given_name = self.request.data['given_name']
        date_birth = self.request.data['date_birth']
        passport_num = self.request.data['passport_num']
        passport_expire = self.request.data['passport_expire']
        district = self.request.data['district']
        address = self.request.data['address']
        v = VerifyPhone.objects.filter(phone=phone, code=code).first()
        if v:
            v.delete()
        else:
            return response.Response({'message': "Confirmation code incorrect!"}, status=status.HTTP_400_BAD_REQUEST)
        # distric = District.objects.filter(id=district).first()
        user = User.objects.create(
            phone=phone,
            name=name,
            last_name=last_name,
            given_name=given_name,
            date_birth=date_birth,
            passport_num=passport_num,
            passport_expire=passport_expire,
            # district=distric,
            address=address,
            password=password
        )
        user.is_active = True
        user.save()
        token = Token.objects.create(user=user)
        data = {
            'message': 'User verified',
            'token': str(token)
        }
        return response.Response(data, status=status.HTTP_201_CREATED)


class LoginAPI(generics.GenericAPIView):
    def get_queryset(self):
        return User.objects.all()

    def get_serializer_class(self):
        return LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = request.data['phone']
        pas = request.data['password']
        if not User.objects.filter(phone=phone).first():
            return response.Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        user = authenticate(phone=phone, password=pas)
        if not user:
            return response.Response({'message': 'Password incorrect'}, status=status.HTTP_401_UNAUTHORIZED)
        token = Token.objects.get(user=user)
        data = dict()
        data['token'] = token.key
        user_serializer = UserSerializer(user).data
        for k, v in user_serializer.items():
            data[k] = v
        data['success'] = True
        return response.Response(data, status=status.HTTP_200_OK)


class ChangePasswordAPI(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = [TokenAuthentication]

    def patch(self, request, *args, **kwargs):
        user = request.user
        pas1 = request.data['password']
        pas2 = request.data['old_password']
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        if user.check_password(pas2):
            user.set_password(pas1)
            user.save()
            return response.Response({'success': True, 'message': 'Successfully changed password'})
        return response.Response({'message': 'old password incorrect'}, status=400)


class UserAPI(generics.RetrieveDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance=instance, data=self.request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)


class ResetPasswordAPI(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = ResetPasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.validated_data['phone']
        code = str(randint(10000, 100000))
        verify(phone, code)
        VerifyPhone.objects.create(phone=phone, code=code)
        return response.Response({"success": True, 'message': "A confirmation code was sent to the phone number!!!"})


class VerifyPhoneResetPasswordAPI(views.APIView):
    def post(self, request, *args, **kwargs):
        phone = self.request.data['phone']
        code = self.request.data['code']
        v = VerifyPhone.objects.filter(phone=phone, code=code).first()
        if v:
            v.delete()
        else:
            return response.Response({'message': "Confirmation code incorrect!"}, status=status.HTTP_400_BAD_REQUEST)
        return response.Response({'message': "Successfully verified!"})


class ResetPasswordConfirmAPI(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = ResetPasswordConfirmSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        phone = serializer.validated_data['phone']
        pas1 = serializer.validated_data['password']
        serializer.is_valid(raise_exception=True)
        user = User.objects.filter(phone=phone).first()
        user.set_password(pas1)
        user.save()
        return response.Response({'success': True, 'message': "Password restored"})
