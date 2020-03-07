from django.conf.urls import url
from HelloWorld import views
from django.urls import path

app_name = "HelloWorld"

urlpatterns = [
    url(r'^$',views.VarsityLView.as_view(),name='listV'),
    url(r'^(?P<pk>[-\w]+)/$',views.VarsityDView.as_view(),name='detail')
]



