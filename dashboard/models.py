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

class Recipe(models.Model):
    title = models.CharField(max_length=50)
    #image = models.ImageField()
    description =models.TextField()
    time = models.FloatField()
    serves = models.IntegerField()
    ingredients = models.TextField()
    directions =models.TextField()
    feedback =models.TextField()
    #rating =
    keywords = models.CharField(max_length=50)

class User(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

# class Feedback(models.Model):
#         Username = models.Charfield(max_length=50)
#         email = models.EmailField()
#         title = models.Charfield(max_length=120)
#         message = models.Textfield()
#         happy = models.Booleanfield()


