# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-28 19:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderlineitem',
            old_name='products',
            new_name='product',
        ),
    ]