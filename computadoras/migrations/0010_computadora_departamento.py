# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computadoras', '0009_auto_20180918_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='computadora',
            name='departamento',
            field=models.CharField(default=b'Hemeroteca', max_length=50, choices=[(b'Direccion general', b'1'), (b'Sistemas de informacion', b'2'), (b'Recursos humanos', b'3'), (b'Investigacion', b'4'), (b'Evaluacion', b'5'), (b'Hemeroteca', b'6'), (b'Dise\xc3\xb1o y comunicacion', b'7')]),
        ),
    ]
