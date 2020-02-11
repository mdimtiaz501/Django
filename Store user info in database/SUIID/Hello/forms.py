from django import forms
from Hello.models import User_login

class NewUser(forms.ModelForm):
    class Meta():
        model = User_login
        fields = '__all__'









