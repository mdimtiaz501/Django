from django.shortcuts import render
from django.template import Context
from django.http import HttpResponse
from Hello.models import Subject,Webpage,AccessRecord

# Create your views here.
def index(request):
    wp_lists = AccessRecord.objects.order_by('date')
    dictionary = {'access_record' : wp_lists}
    return render(request,'Hello/index.html',context=dictionary)

'''def index(request):
    return render(request,'Hello/index.html')'''