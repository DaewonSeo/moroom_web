# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-14 02:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Door',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('deposit_ori', models.IntegerField()),
                ('rentfee_ori', models.IntegerField()),
                ('deposit_new', models.IntegerField()),
                ('rentfee_new', models.IntegerField()),
                ('manage_fee', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('location_long', models.CharField(max_length=50)),
                ('location_lat', models.CharField(max_length=50)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('contact', models.CharField(max_length=50)),
                ('text', models.TextField(default=' ')),
            ],
        ),
        migrations.CreateModel(
            name='RoomAgree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agreement', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='RoomStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('door', models.ManyToManyField(to='app.Door')),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='room_agree',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.RoomAgree'),
        ),
        migrations.AddField(
            model_name='room',
            name='room_option',
            field=models.ManyToManyField(to='app.Option'),
        ),
        migrations.AddField(
            model_name='room',
            name='room_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.RoomStatus'),
        ),
        migrations.AddField(
            model_name='room',
            name='room_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.RoomType'),
        ),
        migrations.AddField(
            model_name='room',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.University'),
        ),
        migrations.AddField(
            model_name='room',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='photo',
            name='rooms',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo', to='app.Room'),
        ),
    ]
