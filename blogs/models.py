from django.db import models
from django.contrib.auth.models import User



class Topic(models.Model):
    """博客主题"""
    text = models.CharField(max_length=20)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.text



class Post(models.Model):
    """博客文章"""
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)
    topic = models.ForeignKey(Topic)

    def __str__(self):
    	return self.text




		
		
