# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-24 15:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0010_auto_20181023_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='shared_with',
            field=models.ManyToManyField(related_name='shared_lists', to=settings.AUTH_USER_MODEL),
        ),
    ]