# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeSwimming001', '0007_auto_20160624_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='distance',
            field=models.IntegerField(default=50),
            preserve_default=False,
        ),
    ]
