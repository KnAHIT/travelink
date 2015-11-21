# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0007_auto_20151120_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel_plan',
            name='Budget',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='travel_plan',
            name='People_amount',
            field=models.IntegerField(),
        ),
    ]
