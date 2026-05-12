from django.contrib import admin

from .models import Escuela, Curso, Alumno, Asistencia, Observacion

admin.site.register(Escuela)
admin.site.register(Curso)
admin.site.register(Alumno)
admin.site.register(Observacion)


@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('alumno', 'curso', 'fecha_hora', 'presente', 'observacion')