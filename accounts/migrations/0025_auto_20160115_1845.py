# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_user_first_otherprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='wall',
            field=models.ForeignKey(related_name='status_wall_set', to=settings.AUTH_USER_MODEL),
        ),
    ]
