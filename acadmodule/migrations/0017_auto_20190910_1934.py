# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-09-10 14:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acadmodule', '0016_auto_20190910_1933'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='batchsemester',
            unique_together=set([]),
        ),
    ]
