# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computadoras', '0002_computadora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computadora',
            name='operativo',
            field=models.CharField(default=b'Windows 8', max_length=50, choices=[(b'Windows XP', b'Windows XP'), (b'Windows 7', b'Windows 7'), (b'Windows Vista', b'Windows Vista'), (b'Windows 8', b'Windows 8'), (b'Windows 10', b'Windows 10'), (b'Linux OS', b'Linux OS'), (b'Mac OS X', b'Mac OS X'), (b'No especificado', b'No especificado')]),
        ),
    ]
