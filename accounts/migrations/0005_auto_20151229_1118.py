# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20151228_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='likes',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
