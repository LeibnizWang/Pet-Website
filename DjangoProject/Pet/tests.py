# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.shortcuts import render_to_response,HttpResponse
from Pet.models import Guy,sort
from PIL import Image
# Create your tests here.
def op(request):
    for i in range(10):
        user=Guy()
        user.username="北京用户"+str(i+11)
        user.phone=i
        user.city="北京市"
        user.address="理工宿舍#"+str(i+11)
        user.experience="1年以下"
        #user.seed="猫"
        user.seed="狗"
        user.price="100以内/天"
        user.information="###"
        user.animal_info="###"
        user.quantity=0
        user.picture="\static\images\e"+str(i)+".jpg"
        user.score=-1
        user.save()
    return HttpResponse("<p>注册成功！</p>")

def op2(request):
    for i in range(20):
        sort1=sort()
        sort1.username="上海用户"+str(i+1)
        sort1.flag=0
        sort1.save()
    return HttpResponse("<p>注册成功</p>")

#im = Image.open('C:/Users/leibn/Documents/Django Projects/Django0427/Pet/static/images/UserhomeImages/768798.jpg')
#image_resized = im.resize((480,280), Image.ANTIALIAS)
#image_resized.save('C:/Users/leibn/Documents/Django Projects/Django0427/Pet/static/images/UserhomeImages/768798.jpg', 'jpeg')

