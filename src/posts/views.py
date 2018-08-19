from django.http import HTTPResponse
from django.shortcuts import render

# Create your views here.
def posts_home(request):
	return HTTPResponse("<h1>Hello</h1>")
