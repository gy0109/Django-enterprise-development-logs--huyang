# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-06 11:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190505_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content_html',
            field=models.TextField(blank=True, editable=False, verbose_name='正文HTML代码'),
        ),
    ]
