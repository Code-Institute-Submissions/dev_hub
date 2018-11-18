from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Profile


class LoginForm(forms.Form):
    
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
class UserRegistrationForm(UserCreationForm):
    
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
        
    password2 = forms.CharField(label="Password Confirmation", widget=forms.PasswordInput)
        
    class Meta:
        
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]
    
    def clean_email(self):
        
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email address must be unique.")
        return email
        
    def clean_password_confirm(self):
        
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        
        if not password1 or not password2:
            raise forms.ValidationError("Please confirm your password.")
            
        if password1 != password2:
            raise forms.ValidationError("Passwords must match.")
            
        return password2
        
class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ["forum_tag", "avatar"]