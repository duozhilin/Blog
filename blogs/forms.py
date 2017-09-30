from django import forms

from .models import Topic, Post

cols_ = {'cols': 80}


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': '主题'}
        widgets = {'text': forms.TextInput(attrs=cols_)}


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['topic', 'title', 'cover', 'summary', 'text', 'tags']
        labels = {'topic': '主题/分类', 'title': '标题', 'summary': '摘要', 'tags': '标签', 'text': '文本', 'cover': '封面图'}
        widgets = {'topic': forms.Select(attrs=cols_),
                   'title': forms.TextInput(attrs=cols_),
                   'summary': forms.Textarea(attrs=cols_),
                   'tags': forms.TextInput(attrs=cols_),
                   'text': forms.Textarea(attrs=cols_),
                   'cover': forms.TextInput()}
