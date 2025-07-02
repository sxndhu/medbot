from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length = 30, required = True, help_text = 'Enter your first name.')
    last_name = forms.CharField(max_length = 30, required = False, help_text = 'Enter your last name.')
    email = forms.EmailField(max_length = 200, required = True, help_text = 'Please enter a valid email address.')


    class Meta: 
        model = User
        fields = [ 'username' , 'first_name', 'last_name' , 'email' , 'password1' , 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)