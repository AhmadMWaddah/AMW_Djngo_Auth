from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'UserName..'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password..'}))


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'type': 'text', 'name': 'username', 'placeholder': 'UserName..'}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'type': 'email', 'name': 'email', 'placeholder': 'E-Mail..'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'type': 'password', 'name': 'password1', 'placeholder': 'Password..'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'type': 'password', 'name': 'password2', 'placeholder': 'Confirm Password..'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
