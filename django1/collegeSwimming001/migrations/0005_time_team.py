# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeSwimming001', '0004_auto_20160617_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='time',
            name='team',
            field=models.ForeignKey(default=b'', to='collegeSwimming001.Team'),
        ),
    ]
