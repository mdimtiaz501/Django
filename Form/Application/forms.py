from django import forms
from django.core import validators

def check_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("First letter must be z.")

class Any_Form(forms.Form):
    FirstName = forms.CharField()  #FirstName = forms.CharField(validators=[check_z])
    LastName = forms.CharField()
    Email = forms.EmailField()
    Confirm_email = forms.EmailField(label="Enter email again.")
    Address = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['Email']
        confirm_email = all_clean_data['Confirm_email']
        if email != confirm_email:
            raise forms.ValidationError("Confirm Please!")




'''    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
	validators=[validators.MaxLengthValidator(0)])'''

'''    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError("You're a bot")
        return botcatcher   '''
