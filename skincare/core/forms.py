from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUpForm(UserCreationForm):
    password1 =forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'form-control'}))
    password2 =forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password','class':'form-control'}))
    class Meta:
        model= User
        
        fields=['username','last_name','email',]

        labels={'email':'Email','last_name':'Name'}
        widgets={
            'username':forms.TextInput(attrs={'placeholder':'Username','class':'form-control'}), 
            'last_name':forms.TextInput(attrs={'placeholder':'Name','class':'form-control'}), 
            'email':forms.EmailInput(attrs={'placeholder':'Email','class':'form-control'}), 
        }
 