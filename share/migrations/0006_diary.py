# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0005_auto_20151120_1944'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Title', models.CharField(max_length=20, null=True, blank=True)),
                ('Passage', models.TextField(null=True, blank=True)),
                ('Tag', models.CharField(max_length=50, blank=True)),
                ('Date_time', models.DateTimeField(auto_now_add=True)),
                ('Image', models.ImageField(upload_to=b'./upload/diary/', blank=True)),
                ('Destination', models.CharField(max_length=20)),
                ('Username', models.ForeignKey(to='share.Account')),
            ],
            options={
                'ordering': ['-Date_time'],
            },
        ),
    ]
