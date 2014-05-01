from django.conf.urls import patterns, include, url

import views

urlpatterns = patterns('',
	url(r'^signin$', views.sign_in),
	url(r'^signup$', views.sign_up),
	url(r'^signout$', views.sign_out),
)
