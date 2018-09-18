# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computadoras', '0003_auto_20180917_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computadora',
            name='tipo',
            field=models.CharField(default=b'Escritorio', max_length=50, choices=[(b'Escritorio', b'Escritorio'), (b'Portatil', b'Portatil'), (b'No especificado', b'No especificado')]),
        ),
    ]
