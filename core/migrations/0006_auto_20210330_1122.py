# Generated by Django 2.1.7 on 2021-03-30 14:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20190325_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 3, 30, 11, 22, 11, 81130)),
        ),
    ]
