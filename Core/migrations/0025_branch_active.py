# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-01 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0024_auto_20160901_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
