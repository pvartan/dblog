# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 22:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_blog', '0002_blogpost_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]