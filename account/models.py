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


class CustomUserManager(BaseUserManager):
    def create_superuser(self, email, user_name, first_name, password, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True.")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True.")

        return self.create_user(email, user_name, first_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, password, **other_fields):
        if not email:
            raise ValueError("You must provide an email address")

        email = self.normalize_email(email)
        user = self.model(
            email=email, user_name=user_name, first_name=first_name, **other_fields
        )
        user.set_password(password)
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    user_name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    phone_number = PhoneNumberField(unique=True, null=False, blank=False)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "user_name"
    REQUIRED_FIELDS = ["email", "first_name", "phone_number"]

    def __str__(self):
        return self.user_name
