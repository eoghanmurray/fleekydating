# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20160104_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='university',
            field=models.CharField(max_length=8, null=True, choices=[(b'Trinity', b'Trinity'), (b'DIT', b'DIT'), (b'UCD', b'UCD'), (b'IADT', b'IADT'), (b'NUIG', b'NUIG'), (b'UL', b'UL'), (b'NUI', b'NUI')]),
        ),
    ]
