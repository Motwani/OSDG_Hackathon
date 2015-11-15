# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20151115_1128'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='prof_id',
            new_name='proff',
        ),
    ]
