from django.conf.urls import patterns, url, include
from django.views.generic import DetailView
from .models import Feat, Rockinfo, Rockvids
from . import views



urlpatterns = [
   
  url(r'^$', views.rock_and_feat, name='rock_and_feat'),
  url(r'^featured/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
  url(r'^trending/(?P<pk>[0-9]+)/$', views.NaversDetailView.as_view(), name='navers'),
  url(r'^contact/$', views.contact, name='contact'),
  url(r'^feedback/$', views.feedback, name='feedback'),
  url(r'^rockstars/(?P<pk>[0-9]+)/$', views.RockDetailView.as_view(), name='detailrock'),
  url(r'^contact/feature/accepted/$', views.contact, name='contact'),
  url(r'^genres/(?P<pk>[0-9]+)/$', views.GenreDetailView.as_view(), name='genres'),
  url(r'^about/$', views.about, name='about'),
  url(r'^contact/$', views.contact, name='contact'),
  url(r'^FAQ/$', views.faq, name='faq'),
]
handler404 = 'mysite.views.error404'
handler404 = 'mysite.views.error500'


