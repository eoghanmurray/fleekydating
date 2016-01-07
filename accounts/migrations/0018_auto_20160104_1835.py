# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_auto_20160104_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='living',
            field=models.CharField(max_length=8, null=True, choices=[(b'Dublin', b'Dublin'), (b'Cork', b'Cork'), (b'Galway', b'Galway'), (b'Belfast', b'Belfast'), (b'Limerick', b'Limerick')]),
        ),
    ]
