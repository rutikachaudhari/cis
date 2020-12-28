from django import forms
from .models import UserProfileInfo, User, Category, Product
from django.contrib.auth.models import User
from django.forms import ModelForm

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic',)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
