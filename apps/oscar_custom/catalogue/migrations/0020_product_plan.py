# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-03 03:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0019_remove_product_books'),
        ('core', '0003_auto_20181003_0316'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='plan',
            field=models.ManyToManyField(blank=True, to='core.Payment_Plan', verbose_name='Plan'),
        ),
    ]
