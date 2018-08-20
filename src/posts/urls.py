from django.urls import path
from posts.views import *
from django.conf.urls import url
urlpatterns = [
	url(r'^$', post_list),
	url(r'^create/$', post_create),
	url(r'^(?P<id>\d+)/$', post_detail),
	url(r'^update/$', post_update),
	url(r'^delete/$', post_delete),
]
