# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-20 07:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20161220_0724'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='featured_image',
        ),
        migrations.AddField(
            model_name='post',
            name='content_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]