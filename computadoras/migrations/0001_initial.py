# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('area', models.CharField(max_length=50)),
                ('responsable', models.CharField(max_length=50)),
            ],
        ),
    ]
