from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (UserCreationForm, AuthenticationForm,)



class CustomUserRegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'username']


class CustomUserLoginForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'password']


class CutomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = [ 'email', 'username']

