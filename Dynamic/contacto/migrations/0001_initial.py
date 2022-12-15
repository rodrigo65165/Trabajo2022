# Generated by Django 3.2.13 on 2022-08-01 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ruc', models.CharField(max_length=200)),
                ('representante', models.CharField(max_length=200)),
                ('razonsocial', models.CharField(max_length=200)),
                ('correo', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'solicitud',
                'verbose_name_plural': 'Solicitudes',
                'ordering': ['-created'],
            },
        ),
    ]
