# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# Create your views here.
ctx={}

def index(request):
    return redirect("/Pet/index")
