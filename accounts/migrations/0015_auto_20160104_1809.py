# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_remove_user_dislikes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='likes',
            field=models.CharField(max_length=8, null=True, choices=[(b'Male', b'Male'), (b'Female', b'Female')]),
        ),
    ]
