# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 00:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_import', '0018_auto_20160725_0359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newdatafileaccesslog',
            name='ip_address',
            field=models.GenericIPAddressField(null=True),
        ),
    ]
