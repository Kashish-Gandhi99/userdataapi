#!/usr/bin/python
# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):

    activity = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:

        model = User
        fields = ('id', 'name', 'timezone', 'activity')
