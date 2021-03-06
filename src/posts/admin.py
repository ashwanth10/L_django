from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
	search_fields = ['title', 'content',]
	list_display = ['__unicode__','timestamp',]
	class Meta():
		model = Post

admin.site.register(Post, PostAdmin)