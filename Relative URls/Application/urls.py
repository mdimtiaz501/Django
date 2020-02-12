from django.conf.urls import url,include
from Application import views

app_name = 'Application'

urlpatterns = [
    url(r'^about/$',views.about_us,name='aboutus'),
    url(r'^home/$',views.home,name='home')
]