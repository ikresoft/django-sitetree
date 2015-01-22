# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitetree', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treeitem',
            name='title',
            field=models.CharField(help_text='Site tree item title. Can contain template variables E.g.: {{ mytitle }}.', max_length=200, verbose_name='Title'),
            preserve_default=True,
        ),
    ]
