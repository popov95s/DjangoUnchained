# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeSwimming001', '0014_auto_20160704_1028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event',
        ),
        migrations.AddField(
            model_name='event',
            name='stroke',
            field=models.CharField(default='Free', max_length=10, choices=[(b'1', b'Freestyle'), (b'2', b'Backstroke'), (b'3', b'Breaststroke'), (b'4', b'Butterfly'), (b'5', b'Individual Medley')]),
            preserve_default=False,
        ),
    ]
