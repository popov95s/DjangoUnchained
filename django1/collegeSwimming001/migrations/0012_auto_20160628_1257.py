# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeSwimming001', '0011_team_abbreviation'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='city',
            field=models.CharField(default=b'', max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='team',
            name='state',
            field=models.CharField(default=b'', max_length=2, blank=True),
        ),
    ]
