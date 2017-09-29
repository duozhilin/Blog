from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, Http404

from .models import Post, Topic


def index(request):
	"""系统主题"""
	posts = Post.objects.order_by('-date_added')
    context = {'posts':posts}
    return render(request, 'blogs/index.html', context)


def user_index(request):
	"""当前用户主页"""
    posts=[]
    if request.user.is_authenticated():
        posts = Post.objects.filter(owner=request.user).order_by('-date_added')
    context = {'posts':posts}
    return render(request, 'blogs/user_index.html', context)


def posts_user(request, user_id):
	"""指定用户主页"""
    user = User.objects.get(id=user_id)
    if user:
	    posts = Post.objects.filter(owner=request.user).order_by('-date_added')
	    context = {'posts':posts, 'user':user}
	    return render(request, 'blogs/index.html', context)
	else:
		raise Http404


def post(request, post_id):
	"""文章页"""
	post = Post.objects.filter(owner=request.user).get(id=post_id)
	if post:
		context = {'post':post}
		return render(request, 'blogs/post.html', context)
	else:
		raise Http404

