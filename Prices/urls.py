from django.conf.urls import patterns, include, url
from Prices import views

urlpatterns = patterns('',
    # ex: /Prices/
    url(r'^$', views.index, name='index'),
    
)