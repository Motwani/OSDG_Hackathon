# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_prof_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prof',
            name='clarity',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='prof',
            name='dedicated',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='prof',
            name='friendly',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='prof',
            name='helpfullness',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='prof',
            name='noofratings',
            field=models.IntegerField(default=0),
        ),
    ]
