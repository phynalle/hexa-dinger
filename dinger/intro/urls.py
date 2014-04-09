from django.conf.urls import patterns, include, url

from intro import views

urlpatterns = patterns('',
	url(r'^$', views.intro, name="index"),
)