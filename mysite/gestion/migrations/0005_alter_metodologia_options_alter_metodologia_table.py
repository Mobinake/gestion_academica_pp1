# Generated by Django 5.0.4 on 2024-10-09 00:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0004_alter_tipo_evaluacion_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='metodologia',
            options={'ordering': ['id_metodologia', 'nombre_metodologia'], 'verbose_name': 'Metodologia', 'verbose_name_plural': 'Metodologias'},
        ),
        migrations.AlterModelTable(
            name='metodologia',
            table='metodologia',
        ),
    ]
