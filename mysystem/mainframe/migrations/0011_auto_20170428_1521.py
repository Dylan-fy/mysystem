# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainframe', '0010_auto_20170428_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(default=b'\xe7\x94\xb7', max_length=3, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(b'1', b'\xe7\x94\xb7'), (b'1', b'\xe5\xa5\xb3'), (b'1', b'\xe6\x9c\xaa\xe7\x9f\xa5')]),
            preserve_default=True,
        ),
    ]
