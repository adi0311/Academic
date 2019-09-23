# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-09-09 16:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acadmodule', '0007_auto_20190909_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='btechcurriculum',
            name='Core_design_credit',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='btechcurriculum',
            name='Core_engineering_science_credit',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='btechcurriculum',
            name='Core_humanities_credit',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='btechcurriculum',
            name='Core_management_science_credit',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='btechcurriculum',
            name='Core_manufacturing_credit',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='btechcurriculum',
            name='Core_natural_science_credit',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='btechcurriculum',
            name='professional_core_credit',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='btechcurriculum',
            name='professional_elective_credit',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='btechcurriculum',
            name='professional_lab_credit',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='btechcurriculum',
            name='professional_project_credit',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='curriculumcourse',
            name='semester',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='acadmodule.BatchSemester'),
        ),
    ]
