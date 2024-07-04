# Generated by Django 5.0.4 on 2024-07-02 18:32

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id_career', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name_career', models.CharField(default=None, max_length=50)),
                ('faculty', models.CharField(default=None, max_length=50)),
            ],
            options={
                'verbose_name': 'Carrera',
                'verbose_name_plural': 'Carreras',
                'db_table': 'career',
                'ordering': ['id_career', 'name_career'],
            },
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id_period', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name_period', models.CharField(max_length=50)),
                ('year_period', models.DateTimeField(auto_now_add=True)),
                ('semester_period', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name': 'Periodo Academico',
                'verbose_name_plural': 'Periodos Academicos',
                'db_table': 'period',
                'ordering': ['id_period', 'year_period'],
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('ci', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('birth_date', models.DateField(default=django.utils.timezone.now)),
                ('address', models.CharField(default=None, max_length=50)),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
                'db_table': 'person',
                'ordering': ['first_name', 'last_name'],
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id_schedule', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('day', models.CharField(choices=[('LUN', 'Lunes'), ('MAR', 'Martes'), ('MIE', 'Miércoles'), ('JUE', 'Jueves'), ('VIE', 'Viernes'), ('SAB', 'Sábado'), ('DOM', 'Domingo')], default='LUN', max_length=10)),
                ('time_start', models.TimeField(default='09:00')),
                ('time_end', models.TimeField(default='12:00')),
            ],
            options={
                'verbose_name': 'Horario',
                'verbose_name_plural': 'Horarios',
                'db_table': 'schedule',
                'ordering': ['id_subject', 'day'],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id_course', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=50)),
                ('id_career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.career')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
                'db_table': 'course',
                'ordering': ['id_course', 'course_name'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_user', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('user_type', models.CharField(choices=[('EST', 'Estudiante'), ('PRO', 'Profesor'), ('ADM', 'Administrativo')], default='EST', max_length=3)),
                ('ci', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.person')),
                ('id_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'user',
                'ordering': ['id_user', 'ci'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id_student', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True)),
                ('assistance', models.BooleanField(default=False)),
                ('behaviour', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('ci', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.person')),
                ('id_career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.career')),
            ],
            options={
                'verbose_name': 'Estudiante',
                'verbose_name_plural': 'Estudiantes',
                'db_table': 'student',
                'ordering': ['id_student', 'ci'],
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id_subject', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name_subject', models.CharField(default=None, max_length=50)),
                ('id_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.course')),
                ('id_period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.period')),
                ('id_schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.schedule')),
            ],
            options={
                'verbose_name': 'Asignatura',
                'verbose_name_plural': 'Asignaturas',
                'db_table': 'subject',
                'ordering': ['id_subject'],
            },
        ),
        migrations.AddField(
            model_name='schedule',
            name='id_subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.subject'),
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id_registration', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('account_state', models.CharField(choices=[('AD', 'Al dia'), ('D1', 'Debe 1 cuota'), ('D2', 'Debe 2 cuotas'), ('D3', 'Debe 3 cuotas'), ('D4', 'Debe 4 cuotas'), ('D5', 'Debe 5 cuotas')], default=None, max_length=15)),
                ('id_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.student')),
                ('id_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.subject')),
            ],
            options={
                'verbose_name': 'Matricula',
                'verbose_name_plural': 'Matriculas',
                'db_table': 'registration',
                'ordering': ['id_registration', 'id_student', 'id_subject'],
            },
        ),
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id_grades', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('note', models.TextField(default=None)),
                ('evaluation_date', models.DateTimeField(auto_now_add=True)),
                ('evaluation_type', models.IntegerField(choices=[('ESC', 'Escrito'), ('ORAL', 'Oral'), ('PRAC', 'Practico'), ('MX', 'Mixto')], default='ESC')),
                ('id_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.course')),
                ('id_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.student')),
                ('id_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.subject')),
            ],
            options={
                'verbose_name': 'Calificación',
                'verbose_name_plural': 'Calificaciones',
                'db_table': 'grades',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id_teacher', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('specialization', models.CharField(max_length=50)),
                ('ci', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.person')),
                ('id_subject', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gestion.subject')),
            ],
            options={
                'verbose_name': 'Profesor',
                'verbose_name_plural': 'Profesores',
                'db_table': 'teacher',
                'ordering': ['id_teacher', 'ci'],
            },
        ),
        migrations.AddField(
            model_name='subject',
            name='id_teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.teacher'),
        ),
    ]
