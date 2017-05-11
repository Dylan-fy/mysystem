# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainframe', '0021_auto_20170511_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(max_length=4, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[('\u7537', '\u7537'), ('\u5973', '\u5973')]),
            preserve_default=True,
        ),
    ]
