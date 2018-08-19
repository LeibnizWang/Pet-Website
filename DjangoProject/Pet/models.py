# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.
class Guy(models.Model):
    objects=models.Manager()
    username=models.CharField(max_length=20)
    phone=models.CharField(max_length=11)
    address=models.CharField(max_length=40)
    experience=models.CharField(max_length=20)
    city=models.CharField(max_length=20,default='北京市')
    seed=models.CharField(max_length=20)
    price=models.CharField(max_length=20)
    information=models.CharField(max_length=100)
    animal_info=models.CharField(max_length=100)
    picture=models.CharField(max_length=100)
    score=models.IntegerField(default=0)
    quantity=models.IntegerField(default=0)

class Deal(models.Model):
    objects=models.Manager()
    askname=models.CharField(max_length=20)
    receivename=models.CharField(max_length=20)
    seed=models.CharField(max_length=20)
    price=models.CharField(max_length=20)
    time=models.CharField(max_length=20)
    state=models.CharField(max_length=20,default='等待对方确认')
    #receivestate=models.CharField(max_length=20,default='未完成')
    evaluation=models.IntegerField(default=100)
    picture=models.CharField(max_length=100)
    information=models.CharField(max_length=100)

class sort(models.Model):
    objects=models.Manager()
    username=models.CharField(max_length=20)
    result1=models.CharField(max_length=20)
    result2=models.CharField(max_length=20)
    result3=models.CharField(max_length=20)
    result4=models.CharField(max_length=20)
    result5=models.CharField(max_length=20)
    result6=models.CharField(max_length=20)
    result7=models.CharField(max_length=20)
    result8=models.CharField(max_length=20)
    resultname=models.CharField(max_length=200,default='#')
    flag=models.IntegerField(default=0)

class Card(models.Model):
    objects=models.Manager()
    postname=models.CharField(max_length=20)
    title=models.CharField(max_length=20)
    text=models.CharField(max_length=100)
    time=models.CharField(max_length=20)
    comments=models.CharField(max_length=20)
    picture=models.CharField(max_length=20)