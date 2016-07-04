# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('collegeSwimming001', '0008_event_distance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meet',
            old_name='date',
            new_name='startDate',
        ),
        migrations.AddField(
            model_name='meet',
            name='endDate',
            field=models.DateField(default=datetime.datetime(2016, 6, 28, 9, 49, 2, 128000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
