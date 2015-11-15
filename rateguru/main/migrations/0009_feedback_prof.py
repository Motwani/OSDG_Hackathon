# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20151115_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='prof',
            field=models.ForeignKey(default=1, to='main.Prof'),
            preserve_default=False,
        ),
    ]
