# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-03 02:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0017_remove_product_plan'),
        ('core', '0002_auto_20181003_0233'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='books',
            field=models.ManyToManyField(blank=True, to='core.Book', verbose_name='Book'),
        ),
    ]
