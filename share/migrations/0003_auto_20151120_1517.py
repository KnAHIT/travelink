# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0002_blog_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travel_plan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Destination', models.CharField(max_length=20)),
                ('Start_place', models.CharField(max_length=20)),
                ('Start_date', models.DateField()),
                ('End_date', models.DateField()),
                ('People_amount', models.IntegerField(max_length=10)),
                ('Budget', models.IntegerField(max_length=10)),
                ('Demand', models.CharField(max_length=100, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='account',
            name='Travel_plan',
        ),
        migrations.AddField(
            model_name='travel_plan',
            name='Username',
            field=models.ForeignKey(to='share.Account'),
        ),
    ]
