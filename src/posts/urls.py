from django.urls import path
from posts.views import *
from django.conf.urls import url
urlpatterns = [
	url('^$', post_list),
	url('^create/$', post_create),
	url('^detail/$', post_detail),
	url('^update/$', post_update),
	url('^delete/$', post_delete),
]
