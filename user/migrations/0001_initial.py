# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-13 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('user_type', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'user_details',
            },
        ),
    ]