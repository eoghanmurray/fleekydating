# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_status_wall'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_otherprofile',
            field=models.BooleanField(default=True),
        ),
    ]
