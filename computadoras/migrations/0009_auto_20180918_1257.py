# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computadoras', '0008_remove_computadora_nada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computadora',
            name='administrador',
            field=models.CharField(default=b'SOPTEC REDALYC', max_length=50),
        ),
        migrations.AlterField(
            model_name='computadora',
            name='dominio',
            field=models.CharField(default=b'PC77', max_length=50),
        ),
        migrations.AlterField(
            model_name='computadora',
            name='modelo',
            field=models.CharField(default=b'PC77', max_length=50),
        ),
    ]
