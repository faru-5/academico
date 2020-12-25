from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'is_teacher']