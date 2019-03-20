# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('artist', models.CharField(max_length=150)),
                ('album_title', models.CharField(max_length=150)),
                ('genre', models.CharField(max_length=100)),
                ('album_logo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file_type', models.CharField(max_length=10)),
                ('song_title', models.CharField(max_length=150)),
                ('album', models.ForeignKey(to='music.Album')),
            ],
        ),
    ]
