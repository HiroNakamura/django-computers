# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computadoras', '0003_auto_20180921_0911'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('usuario', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('cargo', models.CharField(default=b'CAPTURISTA ', max_length=50, choices=[(b'CAPTURISTA', b'CAPTURISTA'), (b'PROGRAMADOR', b'PROGRAMADOR'), (b'NO ESPECIFICADO', b'NO ESPECIFICADO'), (b'DISENADOR', b'DISENADOR'), (b'SERVICIO SOCIAL', b'SERVICIO SOCIAL'), (b'LIDER DE PROYECTO', b'LIDER DE PROYECTO'), (b'JEFE DE AREA', b'JEFE DE AREA'), (b'SOPORTE TECNICO', b'SOPORTE TECNICO'), (b'INVESTIGADOR', b'INVESTIGADOR'), (b'DIRECTOR GENERAL', b'DIRECTOR GENERAL')])),
                ('computadora', models.ForeignKey(to='computadoras.Equipo')),
            ],
        ),
    ]
