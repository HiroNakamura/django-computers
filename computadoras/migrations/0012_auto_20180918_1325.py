# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computadoras', '0011_auto_20180918_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computadora',
            name='departamento',
            field=models.CharField(default=b'Hemeroteca', max_length=50, choices=[(b'Direccion general', b'Direccion general'), (b'Sistemas de informacion', b'Sistemas de informacion'), (b'Recursos humanos', b'Recursos humanos'), (b'Recursos humanos', b'Recursos humanos'), (b'Evaluacion', b'Evaluacion'), (b'Hemeroteca', b'Hemeroteca'), (b'Dise\xc3\xb1o y comunicacion', b'Dise\xc3\xb1o y comunicacion')]),
        ),
        migrations.AlterField(
            model_name='computadora',
            name='maquina',
            field=models.CharField(default=b'PC77', max_length=50),
        ),
        migrations.AlterField(
            model_name='computadora',
            name='modelo',
            field=models.CharField(max_length=50),
        ),
    ]
