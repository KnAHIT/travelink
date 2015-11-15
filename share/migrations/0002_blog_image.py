# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='Image',
            field=models.ImageField(upload_to=b'./upload/', blank=True),
        ),
    ]
