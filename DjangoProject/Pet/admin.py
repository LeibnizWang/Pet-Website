# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from Pet.models import Guy,Deal,sort,Card
# Register your models here.
admin.site.register(Guy)
admin.site.register(Deal)
admin.site.register(sort)
admin.site.register(Card)