# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computadoras', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Computadora',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('bien', models.CharField(max_length=50)),
                ('arrendado', models.CharField(max_length=50)),
                ('asignado', models.IntegerField(default=0)),
                ('ip', models.GenericIPAddressField(default=b'148.215.24.1')),
                ('dns', models.GenericIPAddressField(default=b'148.215.1.1')),
                ('red', models.CharField(max_length=50)),
                ('operativo', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=50)),
                ('maquina', models.CharField(max_length=50)),
                ('dominio', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('administrador', models.CharField(max_length=50)),
                ('ubicacion', models.CharField(max_length=50)),
                ('actualizada', models.BooleanField(default=False)),
            ],
        ),
    ]
