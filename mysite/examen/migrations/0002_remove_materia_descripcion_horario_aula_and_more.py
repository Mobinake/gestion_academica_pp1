# Generated by Django 5.0.4 on 2024-06-07 21:23

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examen', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materia',
            name='descripcion',
        ),
        migrations.AddField(
            model_name='horario',
            name='aula',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='horario',
            name='materia',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='examen.materia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='materia',
            name='creditos',
            field=models.IntegerField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='materia',
            name='docente',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='materia',
            name='semestre',
            field=models.IntegerField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]