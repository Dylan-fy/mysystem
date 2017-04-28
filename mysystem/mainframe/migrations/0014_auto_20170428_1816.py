# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainframe', '0013_auto_20170428_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.IntegerField(null=True, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(0, '\u7537'), (1, '\u5973')]),
            preserve_default=True,
        ),
    ]
