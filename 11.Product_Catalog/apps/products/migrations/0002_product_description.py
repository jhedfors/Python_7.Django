# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 05:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default=datetime.datetime(2016, 5, 30, 5, 12, 37, 109000, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
    ]
