# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models

class Command(models.Model):
    command = models.CharField(max_length=20)

class SmallTalk(models.Model):
    query = models.CharField(max_length=50)
    response = models.CharField(max_length=50)

