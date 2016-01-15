# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_user_page_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_feed',
            field=models.BooleanField(default=True),
        ),
    ]
