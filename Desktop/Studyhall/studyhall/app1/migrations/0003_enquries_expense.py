# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-16 05:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20180716_0424'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('course', models.TextField(max_length=50)),
                ('contactno', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('dateofexpense', models.DateField()),
                ('name_studyhall', models.CharField(max_length=50)),
            ],
        ),
    ]