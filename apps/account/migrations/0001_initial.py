# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 19:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkedAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitter_user_id', models.CharField(max_length=50)),
                ('twitter_token', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Accounts',
                'verbose_name': 'Account',
            },
        ),
    ]
