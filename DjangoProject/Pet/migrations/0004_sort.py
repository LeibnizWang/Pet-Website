# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-23 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pet', '0003_auto_20180423_1911'),
    ]

    operations = [
        migrations.CreateModel(
            name='sort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('result1', models.CharField(max_length=20)),
                ('result2', models.CharField(max_length=20)),
                ('result3', models.CharField(max_length=20)),
                ('result4', models.CharField(max_length=20)),
                ('result5', models.CharField(max_length=20)),
                ('result6', models.CharField(max_length=20)),
                ('result7', models.CharField(max_length=20)),
                ('result8', models.CharField(max_length=20)),
                ('flag', models.IntegerField(default=0)),
            ],
        ),
    ]
