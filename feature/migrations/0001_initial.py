# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feat',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('image', models.URLField(default='http://blogs-images.forbes.com/robertwood/files/2015/05/Bono.png')),
                ('youtube_link', models.CharField(max_length=300)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Feats',
                'verbose_name': 'Feat',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('fname', models.CharField(default='unknown', max_length=25)),
                ('fmail', models.EmailField(default='unknown@unknown.com', max_length=50)),
                ('msg', models.CharField(default='no msg', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('genre_name', models.CharField(default='Rock', max_length=200)),
                ('genre_img', models.URLField(default='http://blogs-images.forbes.com/robertwood/files/2015/05/Bono.png')),
                ('genre_about', models.CharField(default='This is a good genre', max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Genrevids',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('vid_1', models.CharField(default='Z7JgY9zezj4', max_length=200)),
                ('vid_n1', models.CharField(default='Something Inside Me', max_length=300)),
                ('vid_2', models.CharField(default='TABgNerEro8', max_length=200)),
                ('vid_n2', models.CharField(default='Moonlight Sonata', max_length=300)),
                ('vid_s1', models.CharField(default='Jonathan Reyes Myers', max_length=300)),
                ('vid_s2', models.CharField(default='Beethoven', max_length=300)),
                ('genrename', models.ForeignKey(to='feature.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Navers',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('film', models.CharField(default='4532ssds', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Rockinfo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('rock_name', models.CharField(default='ac/dc', max_length=200)),
                ('rock_img', models.URLField(default='http://blogs-images.forbes.com/robertwood/files/2015/05/Bono.png')),
                ('rank', models.IntegerField(default=0)),
                ('about', models.CharField(default='they are the best', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Rockvids',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('vid_id1', models.CharField(default='Z7JgY9zezj4', max_length=200)),
                ('vid_name1', models.CharField(default='Something Inside Me', max_length=300)),
                ('vid_id2', models.CharField(default='TABgNerEro8', max_length=200)),
                ('vid_name2', models.CharField(default='Moonlight Sonata', max_length=300)),
                ('vid_singer_name1', models.CharField(default='Jonathan Reyes Myers', max_length=300)),
                ('vid_singer_name2', models.CharField(default='Beethoven', max_length=300)),
                ('rockername', models.ForeignKey(to='feature.Rockinfo')),
            ],
        ),
    ]
