# Generated by Django 5.0.4 on 2024-06-28 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0011_alter_subject_options_remove_subject_id_teacher_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrer',
            name='faculty',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='carrer',
            name='name_carrer',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name_subject',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
