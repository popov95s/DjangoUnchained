# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeSwimming001', '0002_auto_20160616_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_type',
        ),
        migrations.AddField(
            model_name='time',
            name='time_type',
            field=models.CharField(default=b'Final', max_length=11, choices=[(b'Prelim', b'Preliminary'), (b'Semi', b'Semi-Final'), (b'Final', b'Final'), (b'Swim-Off', b'Swim-Off'), (b'Time trial', b'Time trial')]),
        ),
    ]
