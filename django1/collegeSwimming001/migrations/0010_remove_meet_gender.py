# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeSwimming001', '0009_auto_20160628_1249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meet',
            name='gender',
        ),
    ]
