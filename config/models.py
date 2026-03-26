from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings

class User(AbstractBaseUser, PermissionsMixin):
    nickname = models.CharField(max_length=30)
    profile_picture = models.ImageField(upload_to='profile', default=None)
    bio = models.CharField(max_length=1000)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

class Group ():
    bio = models.CharField(max_length=1000)
    nickname = models.CharField(max_length=30)

