# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0008_auto_20151120_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel_plan',
            name='Demand',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
