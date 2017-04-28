# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainframe', '0008_auto_20170428_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(max_length=1, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(b'\xe7\x94\xb7', b'M'), (b'\xe5\xa5\xb3', b'F')]),
            preserve_default=True,
        ),
    ]
