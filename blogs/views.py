from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, Http404

from .models import Post, Topic


def index(request):
    posts=[]
    if request.user.is_authenticated():
        posts = Post.objects.filter(owner=request.user).order_by('-date_added')
    context = {'posts':posts}
    return render(request, 'blogs/index.html', context)

def post(request, post_id):
	post = Post.objects.filter(owner=request.user).get(id=post_id)
	if post:
		context = {'post':post}
		return render(request, 'blogs/post.html', context)
	else:
		raise Http404

