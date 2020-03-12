from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,ListView,DetailView,
                CreateView,UpdateView,DeleteView)
from django.urls import reverse_lazy
from . import models

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['injection'] = "Hello People it's CBVs"
        return context

class VarsityLView(ListView):
    model = models.University

class VarsityDView(DetailView):
    #context_object_name = "vrstydview"
    model = models.University
    template_name = 'HelloWorld/university_detail.html'

class CreateUniversity(CreateView):
    fields = ('name','Faculty','Department')
    model = models.University

class UpdateUniversity(UpdateView):
    fields = ('Faculty','Department')
    model = models.University
    
class DeleteUniversity(DeleteView):
    model = models.University
    success_url = reverse_lazy('HelloWorld:listV')