# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeSwimming001', '0006_relaytime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meet',
            name='status',
            field=models.CharField(default=b'N', max_length=1, choices=[(b'C', b'Completed'), (b'I', b'In Progress'), (b'N', b'Not started')]),
        ),
        migrations.AlterField(
            model_name='swimmer',
            name='date_of_birth',
            field=models.DateField(),
        ),
    ]
