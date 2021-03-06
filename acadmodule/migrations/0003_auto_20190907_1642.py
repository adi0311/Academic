# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-09-07 11:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acadmodule', '0002_auto_20190906_0017'),
    ]

    operations = [
        migrations.CreateModel(
            name='BatchSemester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField(default=0)),
                ('total_number_of_courses', models.IntegerField(default=0)),
                ('professional_core_courses', models.IntegerField(default=0)),
                ('professional_elective_courses', models.IntegerField(default=0)),
                ('professional_project_courses', models.IntegerField(default=0)),
                ('professional_lab_courses', models.IntegerField(default=0)),
                ('Core_engineering_science_courses', models.IntegerField(default=0)),
                ('Core_natural_science_courses', models.IntegerField(default=0)),
                ('Core_humanities_courses', models.IntegerField(default=0)),
                ('Core_design_courses', models.IntegerField(default=0)),
                ('Core_manufacturing_courses', models.IntegerField(default=0)),
                ('Core_management_science_courses', models.IntegerField(default=0)),
                ('pbi', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='BtechCurriculum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('programme', models.CharField(choices=[('BTECH', 'BTech'), ('BDES', 'BDes'), ('MTech', 'MTech'), ('MDes', 'MDes'), ('PhD', 'PhD')], max_length=30)),
                ('batch', models.IntegerField(default=2019)),
                ('professional_core_credit', models.IntegerField(default=0)),
                ('professional_elective_credit', models.IntegerField(default=0)),
                ('professional_project_credit', models.IntegerField(default=0)),
                ('professional_lab_credit', models.IntegerField(default=0)),
                ('Core_engineering_science_credit', models.IntegerField(default=0)),
                ('Core_natural_science_credit', models.IntegerField(default=0)),
                ('Core_humanities_credit', models.IntegerField(default=0)),
                ('Core_design_credit', models.IntegerField(default=0)),
                ('Core_manufacturing_credit', models.IntegerField(default=0)),
                ('Core_management_science_credit', models.IntegerField(default=0)),
                ('pbi', models.IntegerField(default=0)),
                ('pr', models.IntegerField(default=0)),
                ('sem1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Semester1', to='acadmodule.BatchSemester')),
                ('sem2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Semester2', to='acadmodule.BatchSemester')),
                ('sem3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Semester3', to='acadmodule.BatchSemester')),
                ('sem4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Semester4', to='acadmodule.BatchSemester')),
                ('sem5', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Semester5', to='acadmodule.BatchSemester')),
                ('sem6', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Semester6', to='acadmodule.BatchSemester')),
                ('sem7', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Semester7', to='acadmodule.BatchSemester')),
                ('sem8', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Semester8', to='acadmodule.BatchSemester')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='curriculum',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='curriculum',
            name='course_id',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Curriculum',
        ),
    ]
