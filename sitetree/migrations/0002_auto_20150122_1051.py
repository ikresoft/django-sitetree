# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitetree', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tree',
            name='title',
            field=models.CharField(help_text='Site tree title for presentational purposes.', max_length=200, verbose_name='Title', blank=True),
            preserve_default=True,
        ),
    ]
