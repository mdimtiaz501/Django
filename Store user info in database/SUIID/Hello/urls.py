from . import views
from django.urls import path
from django.conf.urls import url
from django.conf.urls import include

urlpatterns = [
    path('', views.index, name="index"),
]
