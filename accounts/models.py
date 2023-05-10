from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.core.validators import RegexValidator

phone_regex = RegexValidator(
    regex=r"^998[378]{2}|9[01345789]\d{7}$",
    message="Phone number must be entered in the format: '998 [XX] [XXX XX XX]'. Up to 12 digits allowed."
)


class Region(models.Model):
    name = models.CharField(max_length=123)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=123)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    def create_user(self, phone, password=None, **kwargs):
        if not phone:
            raise TypeError('Invalid phone number')
        user = self.model(phone=phone, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **kwargs):
        if not password:
            raise TypeError('password no')
        user = self.create_user(phone, password, **kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=350)
    last_name = models.CharField(max_length=132, null=True, blank=True)
    given_name = models.CharField(max_length=132, null=True, blank=True)
    date_birth = models.CharField(max_length=132, null=True, blank=True)
    passport_num = models.CharField(max_length=20, null=True, blank=True)
    passport_expire = models.CharField(max_length=20, null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=223, null=True, blank=True)
    phone = models.CharField(validators=[phone_regex], max_length=12, unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'phone'

    def __str__(self):
        return self.phone


class UserDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    education = models.CharField(max_length=40)
    family_status = models.CharField(max_length=333)
    count_child = models.CharField(max_length=50)
    social_status = models.CharField(max_length=333)
    main_problem = models.CharField(max_length=333)
    mental_problem = models.CharField(max_length=333)
    relative_problem = models.CharField(max_length=333)
    husband_problem = models.CharField(max_length=333)
    divorce_problem = models.CharField(max_length=333)
    not_married_problem = models.CharField(max_length=333)
    sexual_problem = models.CharField(max_length=333)
    child_problem = models.CharField(max_length=333)
    work_problem = models.CharField(max_length=333)

    def __str__(self):
        return self.user.phone


class VerifyPhone(models.Model):
    class Meta:
        verbose_name = ("Telefon raqamni tasdiqlash")
        verbose_name_plural = ("Telefon raqam tasdiqlash")

    phone = models.CharField(max_length=15, verbose_name="Telefon raqam")
    code = models.CharField(max_length=10, verbose_name="Kod")

    def __str__(self):
        return self.phone


class UserCard(models.Model):
    user = models.ForeignKey(User, models.CASCADE, related_name='cards')
    number = models.CharField(max_length=16)
    expire_date = models.CharField(max_length=5)
    holder = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.user.phone


class FreeAccounts(models.Model):
    phone = models.CharField(max_length=122, unique=True)

    def __str__(self):
        return self.phone
