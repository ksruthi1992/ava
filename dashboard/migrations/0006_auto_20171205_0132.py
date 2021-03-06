# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-05 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_userbookmarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direction',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='message',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='serves',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='time',
            field=models.CharField(max_length=10),
        ),
    ]
