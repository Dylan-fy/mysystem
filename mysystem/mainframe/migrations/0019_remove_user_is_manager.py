# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainframe', '0018_auto_20170428_1833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_manager',
        ),
    ]
