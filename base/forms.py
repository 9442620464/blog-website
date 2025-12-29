from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegistrationFrom(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email']