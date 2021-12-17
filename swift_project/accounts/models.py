from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.validators import ASCIIUsernameValidator
from datetime import datetime


def get_profile_image(instance, filename):
    _format = filename.split(".")[-1]
    return f'profile/{instance.username} {str(datetime.now().isoformat(" ", "seconds")).replace(":", "-")}.{_format}'


def get_default_profile_image():
    return f'profile/default/default_image.png'


class MyManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('User must have an email address')
        if not username:
            raise ValueError('User must have an Username')
        user = self.model(email=self.normalize_email(email),
                          username=ASCIIUsernameValidator(username))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email=email, username=username, password=password)
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.is_prime = True
        return user


class MyAccount(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True, blank=False, null=False)
    email = models.EmailField(max_length=128, unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=150, blank=False, null=False)
    last_name = models.CharField(max_length=150, blank=False, null=False)
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to=get_profile_image, blank=True, null=True)

    date_joined = models.DateField(auto_now_add=True)
    last_login = models.DateField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_prime = models.BooleanField(default=False)

    class Meta:
        ordering = ('is_admin',)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

