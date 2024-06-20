from django.db import models

# Modelos
class Estudiante(models.Model):
    first_name = models.CharField(max_length=50, default="desconocido")
    last_name = models.CharField(max_length=50, default="desconocido")
    birth_date = models.DateField(default="2024-07-01")
    email = models.EmailField(default="email")
    phone = models.CharField(max_length=50, default="0")
    address = models.CharField(max_length=50, default="desconocido")
    enrollment_date = models.DateField(default='2024-07-01')
    class Meta:
        db_table = 'estudiante'
        verbose_name_plural = 'Estudiantes'
        verbose_name = 'Estudiante'
        ordering = ['first_name', 'last_name']
        permissions = [
            ("can_view_grades", "Puede ver sus calificaciones"),
            ("can_edit_profile", "Puede editar su perfil"),
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Profesor(models.Model):
    first_name = models.CharField(max_length=50, default="desconocido")
    last_name = models.CharField(max_length=50, default="desconocido")
    hire_date = models.DateField(default='2024-07-01')
    specialization = models.CharField(max_length=100, default="desconocido")
    class Meta:
        verbose_name_plural = 'Profesores'
        verbose_name = 'Profesor'
        ordering = ['first_name', 'last_name']
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.specialization}"

class Curso(models.Model):
    name = models.CharField(max_length=50, default="unknow")
    description = models.TextField(default="Vacio")
    teacher = models.ForeignKey(Profesor, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural= 'Cursos'
        verbose_name = 'Curso'
        ordering = ['name']
    def __str__(self):
        return self.name

class Matricula(models.Model):
    student = models.ForeignKey(Estudiante, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True, blank=True)
    enrollment_date = models.DateField(default='2024-07-01')
    class Meta:
        verbose_name_plural = 'Matriculas'
        verbose_name = 'Matricula'
        ordering = ['student', 'course']
    def __str__(self):
        return f"{self.student} enrolled in {self.course} on {self.enrollment_date}"

class Asignatura(models.Model):
    name = models.CharField(max_length=100, default="unknow")
    course = models.ForeignKey(Curso, related_name='subjects', on_delete=models.CASCADE, null=True)
    class Meta:
        verbose_name_plural = 'Asignaturas'
        verbose_name = 'Asignatura'
        ordering = ['name']
    def __str__(self):
        return self.name

class Nota(models.Model):
    student = models.ForeignKey(Estudiante, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True)
    grade = models.CharField(max_length=2, default=" ", null=True, blank=True)
    class Meta:
        verbose_name_plural = 'Notas'
        verbose_name = 'Nota'
        ordering = ['student', 'course']
    def __str__(self):
        return f"{self.student} - {self.course} : {self.grade}"