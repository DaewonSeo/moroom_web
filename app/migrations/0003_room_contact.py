# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-15 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180215_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='contact',
            field=models.CharField(default='SOME STRING', max_length=50),
            preserve_default=False,
        ),
    ]
