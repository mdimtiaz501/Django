from django.conf.urls import url
from HelloWorld import views
from django.urls import path

app_name = "HelloWorld"

urlpatterns = [
    url(r'^$',views.VarsityLView.as_view(),name='listV'),
    url(r'^(?P<pk>\d+)/$',views.VarsityDView.as_view(),name='detail'),
    url(r'^create/$',views.CreateUniversity.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)/$',views.UpdateUniversity.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.DeleteUniversity.as_view(),name='delete'),
]



