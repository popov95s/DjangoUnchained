# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeSwimming001', '0012_auto_20160628_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='swimmer',
            name='gender',
            field=models.CharField(default=b'', max_length=1, choices=[(b'M', b'Men'), (b'W', b'Women')]),
        ),
    ]
