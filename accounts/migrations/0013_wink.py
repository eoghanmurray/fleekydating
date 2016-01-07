# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_user_first_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('initiator', models.ForeignKey(related_name='wink_initiator_set', to=settings.AUTH_USER_MODEL)),
                ('receiver', models.ForeignKey(related_name='wink_receiver_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
