# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainframe', '0011_auto_20170428_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(default=b'\xe7\x94\xb7', max_length=3, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[('1', '\u7537'), ('1', '\u5973'), ('1', '\u672a\u77e5')]),
            preserve_default=True,
        ),
    ]
