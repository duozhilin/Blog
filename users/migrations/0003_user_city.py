# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 02:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20170930_0611'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(default=1, max_length=20, verbose_name='城市'),
            preserve_default=False,
        ),
    ]
