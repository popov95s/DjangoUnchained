from django.conf.urls import url

from . import views

urlpatterns = [
    # /
    url(r'^$', views.index, name='index'),
    # /event/5/
    url(r'^meet/(?P<meet_id>[0-9]+)/$', views.meet, name='meets'),
	url(r'^swimmer/(?P<swimmer_id>[0-9]+)/$', views.swimmer, name= 'swimmer'),
	url(r'^swimmer/$', views.swimmers, name= 'swimmers'),
	url(r'^meets/$', views.meets, name ='shortMeets'),
	url(r'^meets//$', views.meets2, name ='mediumMeets'),
	url(r'^meets///$', views.meets3, name = 'detailedMeets')
]


