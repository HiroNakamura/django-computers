# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Computadora',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bien', models.CharField(default=b'MXL4332-', max_length=50)),
                ('arrendado', models.CharField(default=b'77', max_length=50)),
                ('asignado', models.IntegerField(default=0)),
                ('ip', models.GenericIPAddressField(default=b'148.215.24.1')),
                ('dns', models.GenericIPAddressField(default=b'148.215.1.1')),
                ('red', models.CharField(max_length=50)),
                ('operativo', models.CharField(default=b'Windows 8', max_length=50, choices=[(b'Windows XP', b'Windows XP'), (b'Windows 7', b'Windows 7'), (b'Windows Vista', b'Windows Vista'), (b'Windows 8', b'Windows 8'), (b'Windows 10', b'Windows 10'), (b'Linux OS', b'Linux OS'), (b'Mac OS X', b'Mac OS X'), (b'No especificado', b'No especificado')])),
                ('tipo', models.CharField(default=b'Escritorio', max_length=50, choices=[(b'Escritorio', b'Escritorio'), (b'Portatil', b'Portatil'), (b'No especificado', b'No especificado')])),
                ('maquina', models.CharField(default=b'PC77', max_length=50)),
                ('dominio', models.CharField(default=b'PC77', max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('administrador', models.CharField(default=b'SOPTEC REDALYC', max_length=50)),
                ('ubicacion', models.CharField(default=b'PISO 2', max_length=50, choices=[(b'PISO 1', b'PISO 1'), (b'PISO 2', b'PISO 2'), (b'PISO 3', b'PISO 3'), (b'PISO 4', b'PISO 4'), (b'PISO 0', b'PISO 0')])),
                ('actualizada', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area', models.CharField(max_length=50)),
                ('responsable', models.CharField(max_length=50)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='computadora',
            name='departamento',
            field=models.ForeignKey(to='computadoras.Departamento'),
        ),
        migrations.AddField(
            model_name='computadora',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
