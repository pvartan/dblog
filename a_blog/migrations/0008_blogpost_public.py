# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_blog', '0007_blogpost_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='public',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]