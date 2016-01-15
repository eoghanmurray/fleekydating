# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_user_first_feed'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='wall',
            field=models.ForeignKey(related_name='status_wall_set', default=0, to=settings.AUTH_USER_MODEL),
        ),
    ]
