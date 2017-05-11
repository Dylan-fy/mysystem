# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainframe', '0019_remove_user_is_manager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='computer',
            name='memory',
        ),
        migrations.RemoveField(
            model_name='computer',
            name='state',
        ),
        migrations.AddField(
            model_name='computer',
            name='config',
            field=models.TextField(help_text='\u4e3b\u673a\u914d\u7f6e', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='computer',
            name='ip_address',
            field=models.CharField(default=b'0.0.0.0', help_text='\u4e3b\u673aip\u5730\u5740', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='computer',
            name='password',
            field=models.CharField(default=b'123456', help_text='\u4e3b\u673a\u767b\u5f55\u5bc6\u7801', max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='computer',
            name='username',
            field=models.CharField(default=b'root', help_text='\u4e3b\u673a\u767b\u5f55\u7528\u6237\u540d', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='computer',
            name='user',
            field=models.ForeignKey(related_name='user_computer', to='mainframe.User', help_text='\u7528\u6237'),
            preserve_default=True,
        ),
    ]
