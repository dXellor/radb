from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields) 

#Student
class User(AbstractUser):

    username = None
    email = models.EmailField(max_length=100, unique=True)
    indeks = models.CharField(max_length=15, default="raXX/YYYY")
    prosek = models.FloatField(default=5.00)
    ostvareni_espb = models.IntegerField(default=0)
    is_verified = models.BooleanField(default=False)

    modul_prva_zelja = models.CharField(max_length=50, default="Neopredeljen")
    modul_druga_zelja = models.CharField(max_length=50, default="Neopredeljen")

    upao_na_prvu_zelju = models.BooleanField(default=True)
    upao_na_drugu_zelju = models.BooleanField(default=False)

    modul_score = models.FloatField(default=0)

    hidden = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] 
    
    objects = UserManager()

    def __str__(self):
        return self.email


