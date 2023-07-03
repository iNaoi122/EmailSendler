# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Email(models.Model):
    email = models.EmailField()
    message_id = models.CharField(max_length=50)
    status = models.CharField(max_length=9)
    timestamp = models.DateTimeField()


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField()

    def __str__(self):
        return self.email
