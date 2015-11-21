# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0006_diary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Image',
            field=models.ImageField(null=True, upload_to=b'./upload/', blank=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='Tag',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='diary',
            name='Image',
            field=models.ImageField(null=True, upload_to=b'./upload/diary/', blank=True),
        ),
        migrations.AlterField(
            model_name='diary',
            name='Tag',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
