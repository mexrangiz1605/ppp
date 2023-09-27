from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'field-input'}),label=' Your Username')
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'field-input'}),label='Your Email')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'field-input'}),label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'field-input'}),label='Replay password')


    class Meta:
        model = User
        fields = ['username','email','password1']



class SignInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'field-input'}),label='Your Username')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'field-input'}),label='Password')


    class Meta:
        model = User
        fields = ['username','password']