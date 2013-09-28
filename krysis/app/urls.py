from django.conf.urls import patterns, url

from app import views

urlpatterns = patterns('',

    url(r'^$', views.index, name='index'),
    url(r'^incomingsms/$', views.sms, name='incomingsms'),
    url(r'^incomingcall/$', views.call, name='incomingcall'),
    url(r'^retrieveTexts/$', views.getTexts, name='retrieveTexts'),

)
