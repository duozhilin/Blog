from django.shortcuts import render
from users.models import User
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Post, Topic
from .forms import PostForm


def index(request):
    """系统主页"""
    posts = Post.objects.order_by('-date_added')
    context = {'posts': posts}

    return render(request, 'blogs/index.html', context)


@login_required
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by('-date_added')
    context = {'topics': topics}
    return render(request, 'blogs/topics.html', context)


@login_required
def new_topic(request):
    """添加新主题"""
    if request.method == 'POST':
        topic = Topic()
        topic.text = request.POST['topic']
        topic.owner = request.user
        topic.save()

        return topics(request)

    return render(request, 'blogs/new_topic.html')


@login_required
def delete_topic(request, topic_id):
    """删除主题"""
    topic = Topic.objects.filter(owner=request.user).get(id=topic_id)
    if topic:
        topic.delete()
        return topics(request)
    else:
        raise Http404


def post(request, post_id):
    """文章页"""
    post = Post.objects.get(id=post_id)
    if post:
        context = {'post': post}
        return render(request, 'blogs/post.html', context)
    else:
        raise Http404


def posts_topic(request, topic_id):
    """文章列表"""
    if topic_id:
        topic = Topic.objects.get(id=topic_id)
        posts = Post.objects.filter(topic=topic).order_by('-date_added')
    else:
        posts = []

    context = {'posts': posts}
    return render(request, 'blogs/posts.html', context)


def posts_user(request, username):
    """用户主页"""
    if username:
        target = User.objects.get(username=username)
        if not target:
            raise Http404
    else:
        if request.user.is_authenticated():
            target = request.user
        else:
            raise Http404

    topics = Topic.objects.filter(owner=target).order_by('-date_added')
    posts = Post.objects.filter(owner=target).order_by('-date_added')
    context = {'topics': topics, 'posts': posts, 'target': target}
    return render(request, 'blogs/posts.html', context)


@login_required
def posts_manger(request):
    """文章管理"""
    posts = Post.objects.filter(owner=request.user).order_by('-date_added')

    context = {'posts': posts}
    return render(request, 'blogs/post_manager.html', context)


@login_required
def new_post(request):
    """发布新文章"""
    if request.method == 'POST':
        # form = PostForm(request.POST)
        # new_post = form.save()
        data = request.POST
        title = data['title']
        summary = data['summary']
        tags = data['tags']
        text = data['text']
        cover = data['cover']
        topic = Topic.objects.filter(owner=request.user).get(id=data['topic'])

        new_post = Post()
        new_post.title = title
        new_post.summary = summary
        new_post.tags = tags
        new_post.text = text
        new_post.owner = request.user
        new_post.cover = cover
        new_post.topic = topic
        new_post.save()

        return HttpResponseRedirect(reverse('blogs:post', args=[new_post.id]))
    else:
        form = PostForm()

    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)


@login_required
def delete_post(request, post_id):
    """删除文章"""
    post = Post.objects.filter(owner=request.user).get(id=post_id)
    if post:
        post.delete()
        return posts_user(request)
    else:
        raise Http404


@login_required
def edit_post(request, post_id):
    """编辑文章"""
    if request.method != 'POST':
        post = Post.objects.filter(owner=request.user).get(id=post_id)
        context = {'post': post}
        return render(request, 'blogs/edit_post.html', context)
    else:
        data = request.POST
        title = data['title']
        summary = data['summary']
        tags = data['tags']
        text = data['text']
        cover = data['cover']
        topic = data['topic']

        new_post = Post()
        new_post.id = post_id
        new_post.title = title
        new_post.summary = summary
        new_post.tags = tags
        new_post.text = text
        new_post.owner = request.user
        new_post.cover = cover
        new_post.topic = topic
        new_post.save()

        return HttpResponseRedirect(reverse('blogs:post', args=[new_post.id]))
