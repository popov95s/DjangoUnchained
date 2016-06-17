# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeSwimming001', '0003_auto_20160617_1947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='time',
            name='swimmer',
        ),
        migrations.AddField(
            model_name='time',
            name='swimmer',
            field=models.ForeignKey(default=b'', to='collegeSwimming001.Swimmer'),
        ),
    ]
