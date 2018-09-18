# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computadoras', '0013_auto_20180918_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computadora',
            name='departamento',
            field=models.ForeignKey(to='computadoras.Departamento'),
        ),
    ]
