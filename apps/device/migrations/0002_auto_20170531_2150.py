# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-31 21:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='key',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='device',
            name='uuid',
            field=models.TextField(),
        ),
    ]
