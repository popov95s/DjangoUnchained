from django.conf.urls import url

from . import views

urlpatterns = [
    # /
    url(r'^$', views.index, name='index'),
    # /event/5/
    url(r'^meets/(?P<meet_id>[0-9]+)/$', views.meetDetails, name='meetDetails'),
	url(r'^swimmer/(?P<swimmer_id>[0-9]+)/$', views.swimmer, name= 'swimmer'),
	url(r'^swimmer/$', views.swimmers, name= 'swimmers'),
	url(r'^meets/$', views.meets, name ='meetsList'),
	url(r'^meets/(?P<meet_id>[0-9]+)/(?P<event_id>[0-9]+)/$', views.meetWithEvent, name = 'detailedMeets')
]


