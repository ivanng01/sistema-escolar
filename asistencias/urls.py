from django.urls import path
from .views import (
    tomar_asistencia, 
    lista_cursos, 
    ver_cursos, 
    lista_cursos_observacion,
    alumnos_observacion,
    crear_observacion,
    lista_observaciones,
    nueva_observacion,
    editar_observacion,
    lista_asistencias,
    consultas,
    consultar_asistencias,
    consultar_observaciones,
    )

urlpatterns = [
    path('asistencia/<int:curso_id>/', tomar_asistencia, name='tomar_asistencia'),
    
    path(
    'asistencias/lista/<int:curso_id>/',
    lista_asistencias,
    name='lista_asistencias'
    ),
    
    path('cursos/', lista_cursos, name='lista_cursos'),
    
    path('inicio/', ver_cursos, name='inicio'),
    
    path('observaciones/', lista_cursos_observacion, name='lista_cursos_observacion'),

    path('observaciones/curso/<int:curso_id>/', alumnos_observacion, name='alumnos_observacion'),

    path(
    'observaciones/alumno/<int:alumno_id>/curso/<int:curso_id>/',
    crear_observacion,
    name='crear_observacion'
    ),   

    path(
    'observaciones/lista/<int:curso_id>/',
    lista_observaciones,
    name='lista_observaciones'
    ),

    path(
    'observaciones/nueva/alumno/<int:alumno_id>/curso/<int:curso_id>/',
    nueva_observacion,
    name='nueva_observacion'
    ),

    path(
    'observaciones/editar/<int:observacion_id>/',
    editar_observacion,
    name='editar_observacion'
    ),

    path('consultas/',consultas, name='consultas'),
    path('consultas/asistencias/', consultar_asistencias, name='consultar_asistencias'),
    path('consultas/observaciones/', consultar_observaciones, name='consultar_observaciones'),

]