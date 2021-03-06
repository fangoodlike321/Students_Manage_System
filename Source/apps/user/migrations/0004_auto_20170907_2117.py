# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-07 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20170906_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='居住地址'),
        ),
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='number',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True, verbose_name='学号'),
        ),
    ]
