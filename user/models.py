from django.db import models
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
import re
from django.contrib.auth.models import AbstractUser,  Group, Permission


# Custom validator for password strength
def validate_password_strength(value):
    min_length = 10

    if len(value) < min_length:
        raise ValidationError(f"Password should have at least {min_length} characters.")

    if not re.search(r'[A-Z]', value):
        raise ValidationError(f"Password should contain at least 1 uppercase character.")
    
    if not re.search(r'[0-9]', value):
        raise ValidationError(f"Password should contain at least 1 digit.")
    
    if not re.search(r'[a-z]', value):
        raise ValidationError(f"Password should contain at least 1 lowercase character.")
    
    if not re.search(r'[!@#$%^&*()\-_=+{};:,<.>]', value):
        raise ValidationError(f"Password should have at least 1 special characters.")


# Create your models here.
class UserRegistration(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255, validators=[validate_password_strength])

    USERNAME_FIELD = 'username'

    
    def save(self, *args, **kwargs):
        # Validate password
        # validate_password(self.password)
        validate_password_strength(self.password)
        # Hash password before saving
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
    