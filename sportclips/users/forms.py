from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User, Profile


class UserRegisterForm(UserCreationForm):
    EMPLOYEE_CHOICES = (
        ('manager', 'MANAGER'),
        ('owner', 'OWNER'),
    )
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()
    employee_type = forms.ChoiceField(choices=EMPLOYEE_CHOICES)

    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', 'email', 'phone',
            'employee_type', 'password1', 'password2'
        ]


class UserUpdateForm(forms.ModelForm):
    EMPLOYEE_CHOICES = (
        ('manager', 'MANAGER'),
        ('owner', 'OWNER'),
    )
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()
    employee_type = forms.ChoiceField(choices=EMPLOYEE_CHOICES)

    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name',
            'email', 'phone', 'employee_type'
        ]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
