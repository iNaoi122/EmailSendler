# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.http import HttpResponse
from django.shortcuts import render
from .models import Subscriber
from .tasks import send_email_tasks


# Create your views here.

def main(request):
    subs = Subscriber.objects.all()
    return render(request, 'main.html', context={"objects": subs})


def send_email(request):
    print "Send"
    send_email_tasks.apply_async([request.GET['email']],
                                 eta=datetime.datetime.strptime(request.GET['date'].decode('utf-8'), '%B %d, %Y'))
    return HttpResponse(status=200)


def status(request):
    print "Read"
    print request.GET.get('data')

    return HttpResponse(status=200)
