from django.shortcuts import render
from django.template import Context
from django.http import HttpResponse

# Create your views here.
def index(request):
    dictionary = {'insert_me' : "Hello I\'m imtiaz nice to meet you!"}
    return render(request,'Hello/index.html',context=dictionary)

'''def index(request):
    return render(request,'Hello/index.html')'''