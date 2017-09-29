from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, Http404

from .models import Post, Topic


def index(request):
    """系统主题"""
    posts = Post.objects.order_by('-date_added')
    context = {'posts':posts}
    return render(request, 'blogs/index.html', context)


def user_index(request, username):
    """用户主页"""
    if username:
        user = User.objects.get(username=username)
        if not user:
            raise Http404
    else:
    	if request.user.is_authenticated():
    		user = request.user
    	else:
    		raise Http404

    posts = Post.objects.filter(owner=request.user).order_by('-date_added')
    context = {'posts':posts, 'user':user}
    return render(request, 'blogs/user_index.html', context)


def post(request, post_id):
	"""文章页"""
	post = Post.objects.filter(owner=request.user).get(id=post_id)
	if post:
		context = {'post':post}
		return render(request, 'blogs/post.html', context)
	else:
		raise Http404

