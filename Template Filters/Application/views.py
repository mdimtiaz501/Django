from django.shortcuts import render

# Create your views here.
def index(request):
    dict = {'Key':'Hello key','value':122}
    return render(request,'Application/index.html',context=dict)

def home(request):
    return render(request,'Application/Home.html')

def about_us(request):
    return render(request,'Application/About_us.html')