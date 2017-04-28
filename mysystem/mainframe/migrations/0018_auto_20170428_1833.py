# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainframe', '0017_auto_20170428_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(max_length=4, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[('\u7537', 'boy'), ('\u5973', 'girl')]),
            preserve_default=True,
        ),
    ]
