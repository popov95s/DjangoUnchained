# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeSwimming001', '0010_remove_meet_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='abbreviation',
            field=models.CharField(default=b'', max_length=16),
        ),
    ]
