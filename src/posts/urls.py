from django.urls import path
from posts.views import *
from django.conf.urls import url

app_name = 'posts'

urlpatterns = [
	url(r'^$', post_list, name='list'),
	url(r'^create/$', post_create),
	url(r'^(?P<id>\d+)/$', post_detail, name="detail"),
	url(r'^(?P<id>\d+)/edit/$', post_update, name="update"),
	url(r'^(?P<id>\d+)/delete/$', post_delete),
]
