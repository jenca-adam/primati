# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2020-09-09 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prispevok',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obsah', models.CharField(max_length=1000)),
                ('published', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
