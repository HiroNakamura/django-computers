# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computadoras', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='computadora',
            name='user',
        ),
        migrations.RemoveField(
            model_name='departamento',
            name='user',
        ),
    ]
