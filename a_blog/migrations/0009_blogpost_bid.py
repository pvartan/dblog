# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_blog', '0008_blogpost_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='bid',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]