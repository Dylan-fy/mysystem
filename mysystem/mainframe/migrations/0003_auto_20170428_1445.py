# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainframe', '0002_auto_20170427_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_manager',
            field=models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x98\xaf\xe7\xae\xa1\xe7\x90\x86\xe5\x91\x98'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='sex',
            field=models.CharField(default=b'\xe7\x94\xb7', max_length=3, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(b'1', b'\xe7\x94\xb7'), (b'2', b'\xe5\xa5\xb3'), (b'2', b'\xe6\x9c\xaa\xe7\x9f\xa5')]),
            preserve_default=True,
        ),
    ]
