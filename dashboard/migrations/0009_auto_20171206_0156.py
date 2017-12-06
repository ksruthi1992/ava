# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-06 09:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_recipe_is_removed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pantry',
            name='ingredient',
        ),
        migrations.AddField(
            model_name='pantry',
            name='encoded_pantry_ingredients',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='recipe',
            name='encoded_recipe_ingredients',
            field=models.TextField(default=''),
        ),
    ]