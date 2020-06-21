#!/usr/bin/python
# -*- coding: utf-8 -*-

# Django Lib

from django.shortcuts import render
from django.http import HttpResponse  # to generate httpresponse
from django.http import JsonResponse  # to generate jsonresponse
from django.forms.models import model_to_dict

#REST Lib
#from rest_framework import viewsets
from .serializers import *
from rest_framework import viewsets, mixins

# Models

from .models import *  # importing DB models

# External Lib

import datetime
import pytz  # to get list of all time-zones
from random import randrange
from random import randint

# To produce output to DJANGO REST Framework

class UserViewSet( mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Used this function to populate dummy data in database

'''
def populatedatabase(request):
    names = ['Kashish Gandhi', 'Rakesh Kumar', 'Robin Patel']
    TIMEZONES = pytz.all_timezones  # list of all time-zones
    for name in names:
        User.objects.create(name=name,
                            timezone=TIMEZONES[randrange(len(TIMEZONES))])
        for i in range(0, 2):
            userobject = User.objects.get(name=name)
            hour = randint(0, 22)
            starttime = datetime.datetime(  # datetime object
                2020,
                randint(1, 12),
                randint(1, 30),
                hour,
                randint(0, 59),
                randint(0, 59),
                )
            endtime = datetime.datetime(  # datetime object
                2020,
                randint(1, 12),
                randint(1, 30),
                hour + 1,
                randint(0, 59),
                randint(0, 59),
                )
            useractivityobject = \
                Useractivity.objects.create(userid=userobject,
                    starttime=starttime, endtime=endtime)
    return HttpResponse('Success')
'''