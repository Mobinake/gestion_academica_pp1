# Generated by Django 5.0.4 on 2024-06-28 19:29

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0012_alter_carrer_faculty_alter_carrer_name_carrer_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Carrer',
            new_name='Career',
        ),
        migrations.AlterModelOptions(
            name='career',
            options={'ordering': ['id_career', 'name_career'], 'verbose_name': 'Carrera', 'verbose_name_plural': 'Carreras'},
        ),
        migrations.RenameField(
            model_name='career',
            old_name='id_carrer',
            new_name='id_career',
        ),
        migrations.RenameField(
            model_name='career',
            old_name='name_carrer',
            new_name='name_career',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='id_carrer',
            new_name='id_career',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='id_carrer',
            new_name='id_career',
        ),
        migrations.AlterField(
            model_name='academicperiod',
            name='semester_academicPeriod',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='grades',
            name='note',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='person',
            name='birth_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='registration',
            name='id_subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.subject'),
        ),
        migrations.AlterModelTable(
            name='career',
            table='career',
        ),
    ]
