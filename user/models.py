from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .custom_manager import CustomUserManager
from user.utils import generate_digits_code
from django_countries.fields import CountryField

import uuid
# Create your models here.

class CustomUser(AbstractBaseUser, PermissionsMixin):
    '''
        This model allows for the creation of a custom user with various fields for personal 
        information and verification, with the ability to log in using a email.
    
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=20,unique=True, null=True, blank=True)
    username = models.CharField(null=True, blank=True, max_length=30, editable=False)
    email = models.EmailField(unique=True,null=False, blank=False)
    is_email_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)
    nationality = CountryField(null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)

    marital_statuses = [
        ('SINGLE', 'SINGLE'),
        ('MARRIED', 'MARRIED'),
        ('DIVORCED', 'DIVORCED'),
        ('WIDOWED', 'WIDOWED')
    ]
    marital_status = models.CharField(max_length=30, choices=marital_statuses, null=True, blank=True)

    genders = [
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
    ]
    gender = models.CharField(max_length=30, choices=genders, null=True, blank=True)
    profile_photo = models.ImageField(upload_to="profile-photos", null=True, blank=True)

    verification_statuses = [
        ('UNVERIFIED', 'UNVERIFIED'),
        ('PENDING VERIFICATION', 'PENDING VERIFICATION'),
        ('VERIFIED', 'VERIFIED')
    ]
    verification_status = models.CharField(max_length=30, choices=verification_statuses, default="UNVERIFIED")

    nid_number = models.CharField(max_length=30, null=True, blank=True)
    nid_document = models.ImageField(upload_to="nid_documents", null=True, blank=True)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class Verification(models.Model):
    '''
    This model is useful for generating verification codes that can be sent to users 
    through different channels for authentication and authorization purposes.

    '''
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    code = models.CharField(max_length=6, default=generate_digits_code, unique=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_valid = models.BooleanField(default=True)
    is_used = models.BooleanField(default=False)
    channels = [
        ("PHONE_NUMBER", "PHONE_NUMBER"),
        ("EMAIL", "EMAIL"),
        ("ALL", "ALL"),
    ]
    channel = models.CharField(max_length=30, default="ALL", choices=channels)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.code} - {self.user.phone_number}"