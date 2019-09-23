# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-09-09 16:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acadmodule', '0008_auto_20190909_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='btechcurriculum',
            name='Core_design_credit',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='btechcurriculum',
            name='Core_engineering_science_credit',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='btechcurriculum',
            name='Core_humanities_credit',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='btechcurriculum',
            name='Core_management_science_credit',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='btechcurriculum',
            name='Core_manufacturing_credit',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='btechcurriculum',
            name='Core_natural_science_credit',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='btechcurriculum',
            name='professional_core_credit',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='btechcurriculum',
            name='professional_elective_credit',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='btechcurriculum',
            name='professional_lab_credit',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='btechcurriculum',
            name='professional_project_credit',
            field=models.IntegerField(default=0),
        ),
    ]