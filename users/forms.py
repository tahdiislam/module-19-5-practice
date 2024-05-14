from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id':'required'}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
