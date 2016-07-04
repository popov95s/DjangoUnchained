# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collegeSwimming001', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='swimmer',
            old_name='gradYear',
            new_name='grad_year',
        ),
        migrations.RenameField(
            model_name='swimmer',
            old_name='registrationDate',
            new_name='registration_date',
        ),
        migrations.RemoveField(
            model_name='swimmer',
            name='dateofbirth',
        ),
        migrations.RemoveField(
            model_name='swimmer',
            name='homePhone',
        ),
        migrations.RemoveField(
            model_name='swimmer',
            name='passwordHash',
        ),
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.CharField(default=b'Final', max_length=11, choices=[(b'Prelim', b'Preliminary'), (b'Semi', b'Semi-Final'), (b'Final', b'Final'), (b'Swim-Off', b'Swim-Off'), (b'Time trial', b'Time trial')]),
        ),
        migrations.AddField(
            model_name='swimmer',
            name='date_of_birth',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='swimmer',
            name='home_phone',
            field=models.CharField(default=b'', max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='swimmer',
            name='password_hash',
            field=models.CharField(default=b'', max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='team',
            name='gender',
            field=models.CharField(default=b'', max_length=1, choices=[(b'M', b'Men'), (b'W', b'Women')]),
        ),
        migrations.AlterField(
            model_name='coaches',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_DEFAULT, default=b'', to='collegeSwimming001.Team'),
        ),
        migrations.AlterField(
            model_name='swimmer',
            name='city',
            field=models.CharField(default=b'', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='swimmer',
            name='country',
            field=models.CharField(default=b'', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='swimmer',
            name='email',
            field=models.CharField(default=b'', unique=True, max_length=40, blank=True),
        ),
        migrations.AlterField(
            model_name='swimmer',
            name='facebook',
            field=models.CharField(default=b'', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='swimmer',
            name='salt',
            field=models.CharField(default=b'', max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='swimmer',
            name='state',
            field=models.CharField(default=b'', max_length=2, blank=True),
        ),
        migrations.AlterField(
            model_name='swimmer',
            name='twitter',
            field=models.CharField(default=b'', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='swimmer',
            name='zipcode',
            field=models.CharField(default=b'', max_length=5, blank=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='conference',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_DEFAULT, default=b'', to='collegeSwimming001.Conference'),
        ),
    ]
