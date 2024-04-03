from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import Propietario

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Propietario
        fields = "__all__"