from django.db import models

# Create your models here.
from django.db import models

class Escuela(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - {self.escuela.nombre}"

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cursos = models.ManyToManyField(Curso, related_name='alumnos')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Asistencia(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()
    presente = models.BooleanField()
    observacion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.alumno} - {self.curso} - {self.fecha_hora}"

class Observacion(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField()

    class Meta:
        ordering = ['-fecha_hora']

    def __str__(self):
        return f"{self.alumno} - {self.fecha_hora}"

