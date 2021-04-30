from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from contact.models import ContactModel


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=50)
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]