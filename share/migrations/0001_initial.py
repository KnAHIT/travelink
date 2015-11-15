# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Username', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254, blank=True)),
                ('Travel_plan', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Title', models.CharField(max_length=20)),
                ('Passage', models.TextField(null=True, blank=True)),
                ('Tag', models.CharField(max_length=50, blank=True)),
                ('Date_time', models.DateTimeField(auto_now_add=True)),
                ('Username', models.ForeignKey(to='share.Account')),
            ],
            options={
                'ordering': ['-Date_time'],
            },
        ),
    ]
