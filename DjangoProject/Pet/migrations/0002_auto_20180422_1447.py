# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-22 06:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guy',
            name='city',
            field=models.CharField(default='\u5317\u4eac\u5e02', max_length=20),
        ),
        migrations.AlterField(
            model_name='guy',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
