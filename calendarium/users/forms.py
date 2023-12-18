from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField


class SignupForm(UserCreationForm):
    captcha = CaptchaField()
    email = forms.EmailField(required=True, max_length=50)
    # password1 = forms.CharField(
    #     label = "Password",
    #     widget=forms.PasswordInput,
    #     required=True,
    #     max_length=100,
    #     min_length= 8,
    # )
    # password2 = forms.CharField(
    #     label = "Password ",
    #     widget=forms.PasswordInput,
    #     required=True,
    #     max_length=100,
    #     min_length= 8,
    # )

    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField()
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = CaptchaField()


