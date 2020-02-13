from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'Application/index.html')

def home(request):
    return render(request,'Application/Home.html')

def about_us(request):
    return render(request,'Application/About_us.html')