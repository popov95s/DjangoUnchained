# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeSwimming001', '0005_time_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelayTime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lead_off', models.ForeignKey(related_name='lead_off', default=b'', to='collegeSwimming001.Time')),
                ('legs', models.ManyToManyField(related_name='legs', to='collegeSwimming001.Time')),
            ],
        ),
    ]
