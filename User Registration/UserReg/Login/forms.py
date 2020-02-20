from django import forms
from django.contrib.auth.models import User
from Login.models import UserInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class UserInformation(forms.ModelForm):
    class Meta():
        model = UserInfo
        fields = ('website','profile_picture')




