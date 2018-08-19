# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.shortcuts import render_to_response,HttpResponse
from django.contrib.auth.models import User
# Create your tests here.
def create(request):
    for i in range(20):
        username0="烟台用户"+str(i+1)
        password0="test"
        email0="testuser"+str(i+1)+"@163.com"
        user=User.objects.create_user(username=username0,password=password0,email=email0)
        user.save()
    return HttpResponse("<p>注册成功</p>")