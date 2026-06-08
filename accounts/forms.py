from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(attrs={
            "class": "form-control form-control-sm",
            "placeholder": "you@example.com",
        }),
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        labels = {
            "username": "Username",
            "password1": "Password",
            "password2": "Confirm Password",
        }
        placeholders = {
            "username": "Enter username",
            "password1": "Enter password",
            "password2": "Confirm password",
        }
        for field_name in ["username", "password1", "password2"]:
            self.fields[field_name].label = labels[field_name]
            self.fields[field_name].widget.attrs["class"] = "form-control form-control-sm"
            self.fields[field_name].widget.attrs["placeholder"] = placeholders[field_name]


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
