# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_auto_20160115_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='author',
            field=models.ForeignKey(related_name='status_author_set', to=settings.AUTH_USER_MODEL),
        ),
    ]
