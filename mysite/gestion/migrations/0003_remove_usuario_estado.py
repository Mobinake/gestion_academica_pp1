# Generated by Django 5.0.4 on 2024-09-30 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_rename_nombre_matricula_materia_nombre_matricula_materia_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='estado',
        ),
    ]
