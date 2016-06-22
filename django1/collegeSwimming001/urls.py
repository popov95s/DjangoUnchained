from django.conf.urls import url

from . import views

urlpatterns = [
    # /
    url(r'^$', views.index, name='index'),
    # /event/5/
    url(r'^meet/(?P<meet_id>[0-9]+)/$', views.meet, name='meets')
]

