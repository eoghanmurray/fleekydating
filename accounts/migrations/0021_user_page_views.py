# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_crush_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='page_views',
            field=models.IntegerField(default=0),
        ),
    ]
