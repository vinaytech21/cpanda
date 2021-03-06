# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-22 07:12
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('docfile', models.FileField(blank=True, null=True, upload_to='Product/%Y/%m/%d')),
                ('description', models.CharField(default=False, max_length=160)),
                ('active', models.BooleanField(default=True)),
                ('quantity', models.IntegerField(default=0)),
                ('zip_Code', models.CharField(blank=True, max_length=6)),
                ('address', models.CharField(default=False, max_length=60)),
                ('date_created', models.DateTimeField(default=datetime.datetime(2016, 4, 21, 7, 12, 46, 630346))),
                ('date_Update', models.DateTimeField(default=django.utils.timezone.now)),
                ('expire_date', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'products',
                'ordering': ('docfile',),
            },
        ),
    ]
