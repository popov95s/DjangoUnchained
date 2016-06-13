# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coaches',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event', models.CharField(max_length=10, choices=[(b'Free', b'Freestyle'), (b'Back', b'Backstroke'), (b'Breast', b'Breaststroke'), (b'Fly', b'Butterfly'), (b'IM', b'Individual Medley')])),
                ('course', models.CharField(max_length=3, choices=[(b'SCY', b'Short Course Yards'), (b'SCM', b'Short Course Meters'), (b'LCM', b'Long Course Meters')])),
            ],
        ),
        migrations.CreateModel(
            name='Meet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('gender', models.CharField(max_length=1, choices=[(b'M', b'Men'), (b'W', b'Women')])),
                ('status', models.CharField(max_length=1, choices=[(b'C', b'Completed'), (b'I', b'In Progress'), (b'N', b'Not started')])),
            ],
        ),
        migrations.CreateModel(
            name='Swimmer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('dateofbirth', models.DateField(null=True, blank=True)),
                ('gradYear', models.DateField()),
                ('city', models.CharField(max_length=255, null=True, blank=True)),
                ('state', models.CharField(max_length=2, null=True, blank=True)),
                ('country', models.CharField(max_length=255, null=True, blank=True)),
                ('zipcode', models.CharField(max_length=5, null=True, blank=True)),
                ('homePhone', models.CharField(max_length=10, null=True, blank=True)),
                ('facebook', models.CharField(max_length=255, null=True, blank=True)),
                ('twitter', models.CharField(max_length=255, null=True, blank=True)),
                ('email', models.CharField(max_length=40, unique=True, null=True, blank=True)),
                ('passwordHash', models.CharField(max_length=255, null=True, blank=True)),
                ('salt', models.CharField(max_length=10, null=True, blank=True)),
                ('registrationDate', models.DateField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('conference', models.ForeignKey(to='collegeSwimming001.Conference', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.CharField(max_length=8)),
                ('place', models.PositiveIntegerField()),
                ('points', models.PositiveIntegerField()),
                ('event', models.ForeignKey(to='collegeSwimming001.Event')),
                ('meet', models.ForeignKey(to='collegeSwimming001.Meet')),
                ('swimmer', models.ManyToManyField(to='collegeSwimming001.Swimmer')),
            ],
        ),
        migrations.AddField(
            model_name='swimmer',
            name='teams',
            field=models.ManyToManyField(to='collegeSwimming001.Team'),
        ),
        migrations.AddField(
            model_name='meet',
            name='teams',
            field=models.ManyToManyField(to='collegeSwimming001.Team'),
        ),
        migrations.AddField(
            model_name='conference',
            name='division',
            field=models.ForeignKey(to='collegeSwimming001.Division'),
        ),
        migrations.AddField(
            model_name='coaches',
            name='team',
            field=models.ForeignKey(to='collegeSwimming001.Team'),
        ),
    ]
