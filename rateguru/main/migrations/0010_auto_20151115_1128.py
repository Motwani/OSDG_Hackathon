# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_feedback_prof'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='prof',
            new_name='proff',
        ),
    ]
