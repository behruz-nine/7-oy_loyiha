from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.username
    
