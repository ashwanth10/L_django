from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

from .forms import PostForm
from .models import Post

# Create your views here.
def post_create(request):
	print(request.POST)
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "created form successfully")
		# success showing the post has been created
		return HttpResponseRedirect(instance.get_absolute_url())
		
	context = {
		"form" : form,
	}
	return render(request, "post_form.html", context)

def post_detail(request, id=None):
	instance = get_object_or_404(Post, id=id) # shows 404 if Post with ID=1 is not found
	
	context = {
		"title" : instance.title,
		"instance" : instance,
	}
	return render(request, "post_detail.html", context)

def post_list(request):
	queryset = Post.objects.all() # reads data from database
	context = {
		"title" : "List auth",
		"objectset" : queryset
	}
	return render(request, "post_list.html", context)

def post_update(request, id=None):
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "<a href='#'>form</a> updated", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
	"title" : instance.title,
#	"instance" : instance,
	"form" : form,
	}

	return render(request, 'post_form.html', context)

def post_delete(request, id=None):
	instance = get_object_or_404(Post,id=id)
	instance.delete()
	#messages.success("Deleted successfully")
	return redirect("posts:list")
