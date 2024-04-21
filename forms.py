from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    Name=forms.CharField(label='Name',widget=forms.TextInput(attrs={'class': 'form-control'}))
    username=forms.CharField(label='username',widget=forms.TextInput(attrs={'class': 'form-control'}))
    email=forms.EmailField(label='email',widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1=forms.CharField(label='password',widget=forms.TextInput(attrs={'class': 'form-control'}))
    password2=forms.CharField(label='Confirm Password',widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Mets:
        model = User
        fields = ('Name', 'username', 'email', 'password1', 'password2')
        
    