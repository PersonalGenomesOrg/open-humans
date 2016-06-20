# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-15 21:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_import', '0017_auto_20160229_0333'),
        ('private_sharing', '0027_auto_20160602_1957'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectDataFile',
            fields=[
                ('parent', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='parent_project_data_file', serialize=False, to='data_import.DataFile')),
                ('direct_sharing_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='private_sharing.DataRequestProject')),
            ],
            bases=('data_import.datafile',),
        ),
    ]