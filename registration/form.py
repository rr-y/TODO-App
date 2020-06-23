from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    Email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = ["Email", "username", "password1", "password2"]