# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Email, Subscriber
# Register your models here.
admin.site.register(Email)
admin.site.register(Subscriber)