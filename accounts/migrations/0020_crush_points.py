# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='crush',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
