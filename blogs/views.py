from django.shortcuts import render

from .models import Post, Topic


def index(request):
	return render(request, 'blogs/index.html')


