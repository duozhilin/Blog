# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 06:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogs', '0012_auto_20171009_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
