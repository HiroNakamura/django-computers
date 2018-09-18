# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computadoras', '0004_auto_20180917_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computadora',
            name='ubicacion',
            field=models.CharField(default=b'PISO 2', max_length=50, choices=[(b'PISO 1', b'PISO 1'), (b'PISO 2', b'PISO 2'), (b'PISO 3', b'PISO 3'), (b'PISO 4', b'PISO 4'), (b'PISO 0', b'PISO 0')]),
        ),
    ]
