# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0004_account_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Title',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
