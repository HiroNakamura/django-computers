# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computadoras', '0006_auto_20180918_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='computadora',
            name='nada',
            field=models.CharField(default=b'', max_length=30),
        ),
    ]
