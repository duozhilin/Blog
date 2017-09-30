from django import forms

from .models import Topic, Post


class TopicForm(forms.ModelForm):
	class Meta:
		model = Topic
		fields = ['text']
		labels = {'text':'主题'}


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title','summary','tags','text','cover']
		labels = {}