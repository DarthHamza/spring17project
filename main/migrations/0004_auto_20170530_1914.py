# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-30 19:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20170530_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffee',
            name='powder',
            field=models.ManyToManyField(null=True, to='main.Powder'),
        ),
        migrations.AlterField(
            model_name='coffee',
            name='syrup',
            field=models.ManyToManyField(null=True, to='main.Syrup'),
        ),
    ]
