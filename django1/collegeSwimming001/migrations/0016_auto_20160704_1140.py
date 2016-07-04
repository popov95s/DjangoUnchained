# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeSwimming001', '0015_auto_20160704_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='place',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='time',
            name='points',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
