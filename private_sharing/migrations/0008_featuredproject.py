# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2018-01-05 01:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('private_sharing', '0007_auto_20171220_2038'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='private_sharing.DataRequestProject')),
            ],
        ),
    ]
