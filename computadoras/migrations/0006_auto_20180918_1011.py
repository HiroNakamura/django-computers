# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computadoras', '0005_auto_20180917_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computadora',
            name='arrendado',
            field=models.CharField(default=b'77', max_length=50),
        ),
        migrations.AlterField(
            model_name='computadora',
            name='bien',
            field=models.CharField(default=b'MXL4332-', max_length=50),
        ),
    ]
