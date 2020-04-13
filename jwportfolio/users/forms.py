from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    # Here, we will specify a new field that we need to add to our form
    email = forms.EmailField()  # By default EmailField(true) is set required to true but
    # if your want it to not required you can specify forms.EmailField(False)

    class Meta:  # This Meta class will save a new username in our User model table in database
        # whenever this form validated, it will create a new user.
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
