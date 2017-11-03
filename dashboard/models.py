# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
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
    featured_image = models.URLField()
    description =models.TextField()
    time = models.TimeField()
    serves = models.IntegerField()
    keywords = models.CharField(max_length=50)

class Recipe_Ingredient(models.Model):
    recipe = models.ForeignKey('Recipe')
    ingredient = models.ForeignKey('Ingredient')

class Recipe_Direction(models.Model):
    recipe = models.ForeignKey('Recipe')
    direction = models.ForeignKey('Direction')
    direction_number = models.IntegerField(null=False)

class Direction(models.Model):
    description = models.CharField(max_length=100)

class Ingredient(models.Model):
    name = models.CharField(max_length=50)

class Pantry(models.Model):
    user = models.ForeignKey('User')
    ingredient = models.ForeignKey('Ingredient')

class Feedback(models.Model):
    title = models.CharField(max_length=50)
    message = models.CharField(max_length=50)
    recipe = models.ForeignKey('Recipe')
    user = models.ForeignKey('User')
    VERYBAD = 1
    BAD = 2
    OKAY = 3
    GOOD = 4
    EXCELLENT = 5
    RATING = (
        (VERYBAD, 'Very bad'),
        (BAD, 'Bad'),
        (OKAY, 'Okay'),
        (GOOD, 'Good'),
        (EXCELLENT, 'Excellent'),
    )

    rating = models.IntegerField(choices=RATING)

class User(AbstractUser):
    profile_pic = models.URLField()

