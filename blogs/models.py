from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """博客主题"""
    text = models.CharField(max_length=20)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


# class Tag(models.Model):
#     """文章标签"""
#     text = models.CharField(max_length=20)
#     date_added = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.text
        

class Post(models.Model):
    """博客文章"""
    title = models.CharField(max_length=200)
    summary = models.TextField()
    tags = models.CharField(max_length=100)
    # tags = models.ManyToManyField(Tag, verbose_name="标签")
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)
    #封面图，后面改为上传图片
    cover = models.TextField()
    topic = models.ForeignKey(Topic)

    def __str__(self):
    	return self.title

		
