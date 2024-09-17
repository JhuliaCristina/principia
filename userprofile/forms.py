from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class CustomUserCreationForm(UserCreationForm):
    cpf = forms.CharField(max_length=40, required=True, label="CPF")

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'cpf']