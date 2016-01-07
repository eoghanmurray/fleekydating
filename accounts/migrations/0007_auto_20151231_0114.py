# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_friends'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friends',
            name='friend',
        ),
        migrations.DeleteModel(
            name='Friends',
        ),
    ]
