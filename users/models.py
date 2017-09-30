from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nickname = models.CharField(max_length=20, unique=True, verbose_name='昵称')
    real_name = models.CharField(max_length=20, verbose_name='姓名')
    id_card = models.CharField(max_length=20, verbose_name='身份证号')

    def get_full_name(self):
        if self.nickname:
            return self.nickname
        else:
            return self.username

    def get_short_name(self):
        if self.nickname:
            return self.nickname
        else:
            return self.username
