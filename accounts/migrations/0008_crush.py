# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20151231_0114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crush',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(related_name='crush_creator_set', to=settings.AUTH_USER_MODEL)),
                ('crush', models.ForeignKey(related_name='crush_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
