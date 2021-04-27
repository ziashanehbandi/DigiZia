from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50,required=False,help_text='optional')
    last_name = forms.CharField(max_length=50,required=False,help_text='optional')
    email = forms.EmailField(max_length=150,required='Required. Inform a valid email address.')

    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2']


