# Generated by Django 5.0.3 on 2024-05-31 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Articles', '0005_delete_articulos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=30)),
                ('score', models.SmallIntegerField(default=0)),
                ('text', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
