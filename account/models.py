from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
    UserManager,
)
from django.core.exceptions import ValidationError
from django.db import models
from django.forms import ValidationError
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class CustomUserManager(UserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        if not password:
            raise ValidationError("password required")
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(
            email=email, password=password, is_staff=True, is_superuser=True
        )
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    phone_number = PhoneNumberField(unique=True, null=False, blank=False)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "username"
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()
