# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0003_auto_20151120_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='Image',
            field=models.ImageField(upload_to=b'./upload/headimage/', blank=True),
        ),
    ]
