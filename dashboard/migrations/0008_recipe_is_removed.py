# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-05 10:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_recipe_ingredients_display'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='is_removed',
            field=models.BooleanField(default=False),
        ),
    ]