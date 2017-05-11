# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainframe', '0020_auto_20170510_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='config',
            field=models.TextField(null=True, verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe9\x85\x8d\xe7\xbd\xae', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='computer',
            name='ip_address',
            field=models.CharField(default=b'0.0.0.0', max_length=50, verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xbaip\xe5\x9c\xb0\xe5\x9d\x80'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='computer',
            name='password',
            field=models.CharField(default=b'123456', max_length=100, verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe7\x99\xbb\xe5\xbd\x95\xe5\xaf\x86\xe7\xa0\x81'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='computer',
            name='user',
            field=models.ForeignKey(related_name='user_computer', verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7', to='mainframe.User'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='computer',
            name='username',
            field=models.CharField(default=b'root', max_length=100, verbose_name=b'\xe4\xb8\xbb\xe6\x9c\xba\xe7\x99\xbb\xe5\xbd\x95\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d'),
            preserve_default=True,
        ),
    ]
