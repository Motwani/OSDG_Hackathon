# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20151115_0123'),
    ]

    operations = [
        migrations.AddField(
            model_name='prof',
            name='clarity',
            field=models.FloatField(default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prof',
            name='dedicated',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prof',
            name='friendly',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prof',
            name='helpfullness',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prof',
            name='noofratings',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
