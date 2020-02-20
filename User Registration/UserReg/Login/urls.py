from django.conf.urls import url
from Login import views

#Template URLs

app_name = 'Login'

urlpatterns = [
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.loginviews,name='user_login'),
    
]