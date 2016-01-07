# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20160104_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='likes',
            field=models.CharField(max_length=8, null=True, choices=[(b'Athletic', b'Athletic'), (b'Academic', b'Academic'), (b'Musical', b'Musical')]),
        ),
    ]
