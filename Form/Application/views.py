from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request,'Application/index.html')

def simple_form(request):
    form = forms.Any_Form()
    if request.method == 'POST':
        form = forms.Any_Form(request.POST)

        if form.is_valid():
            print("Validation success")
            print(form.cleaned_data['FirstName'])
            print(form.cleaned_data['LastName'])
            print(form.cleaned_data['Email'])
            print(form.cleaned_data['Address'])

    return render(request,'Application/form.html',{'form':form})






