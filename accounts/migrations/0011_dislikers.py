# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_likers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dislikers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('disliker', models.ForeignKey(related_name='disliker', to=settings.AUTH_USER_MODEL)),
                ('status', models.ForeignKey(to='accounts.Status')),
            ],
        ),
    ]
