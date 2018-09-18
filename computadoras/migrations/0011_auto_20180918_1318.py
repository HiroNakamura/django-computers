# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computadoras', '0010_computadora_departamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computadora',
            name='departamento',
            field=models.CharField(default=b'Hemeroteca', max_length=50, choices=[(b'1', b'Direccion general'), (b'2', b'Sistemas de informacion'), (b'3', b'Recursos humanos'), (b'4', b'Investigacion'), (b'5', b'Evaluacion'), (b'6', b'Hemeroteca'), (b'7', b'Dise\xc3\xb1o y comunicacion')]),
        ),
    ]
