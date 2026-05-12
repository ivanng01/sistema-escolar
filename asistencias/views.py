from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Alumno, Curso, Asistencia, Observacion
from django.utils import timezone

def tomar_asistencia(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    alumnos = curso.alumnos.all()

    if request.method == 'POST':
        fecha_hora = request.POST.get('fecha_hora')
        presentes_ids = request.POST.getlist('presentes')

        for alumno in alumnos:
            presente = str(alumno.id) in presentes_ids

            Asistencia.objects.create(
                alumno=alumno,
                curso=curso,
                fecha_hora=fecha_hora,
                presente=presente
            )

        return redirect('inicio')

    return render(request, 'asistencias/asistencia.html', {
        'curso': curso,
        'alumnos': alumnos
    })

def lista_asistencias(request, curso_id):

    curso = get_object_or_404(Curso, id=curso_id)

    asistencias = Asistencia.objects.filter(
        curso=curso
    ).order_by('-fecha_hora')

    return render(
        request,
        'asistencias/lista_asistencias.html',
        {
            'curso': curso,
            'asistencias': asistencias
        }
    )

def lista_cursos(request):
    cursos = Curso.objects.all()

    return render(request, 'asistencias/cursos.html', {
        'cursos': cursos
    })

def ver_cursos(request):
    cursos = Curso.objects.all()

    return render(request, 'asistencias/inicio.html', {
        'cursos': cursos
    })

def lista_cursos_observacion(request):

    cursos = Curso.objects.all()

    return render(request, 'asistencias/cursos_observacion.html', {
        'cursos': cursos
    })

def alumnos_observacion(request, curso_id):

    curso = get_object_or_404(Curso, id=curso_id)

    alumnos = curso.alumnos.all()

    return render(request, 'asistencias/alumnos_observacion.html', {
        'curso': curso,
        'alumnos': alumnos
    })

def crear_observacion(request, alumno_id, curso_id):

    alumno = get_object_or_404(Alumno, id=alumno_id)

    curso = get_object_or_404(Curso, id=curso_id)

    if request.method == 'POST':

        descripcion = request.POST.get('descripcion')

        Observacion.objects.create(
            alumno=alumno,
            curso=curso,
            fecha_hora=timezone.now(),
            descripcion=descripcion
        )

    return render(request, 'asistencias/crear_observacion.html', {
        'alumno': alumno,
        'curso': curso
    }
)

def nueva_observacion(request, alumno_id, curso_id):

    alumno = get_object_or_404(Alumno, id=alumno_id)

    curso = get_object_or_404(Curso, id=curso_id)

    if request.method == 'POST':

        descripcion = request.POST.get('descripcion')

        Observacion.objects.create(
            alumno=alumno,
            curso=curso,
            fecha_hora=timezone.now(),
            descripcion=descripcion
        )

        return redirect(f'/observaciones/lista/{curso.id}/')

    return render(request, 'asistencias/nueva_observacion.html', {
        'alumno': alumno,
        'curso': curso
})

def editar_observacion(request, observacion_id):

    observacion = get_object_or_404(
        Observacion,
        id=observacion_id
    )

    if request.method == 'POST':

        descripcion = request.POST.get('descripcion')

        observacion.descripcion = descripcion

        observacion.save()

        return redirect(
            f'/observaciones/lista/{observacion.curso.id}/'
        )

    return render(
        request,
        'asistencias/editar_observacion.html',
        {
            'observacion': observacion
        }
)

def lista_observaciones(request, curso_id):

    curso = get_object_or_404(Curso, id=curso_id)

    alumnos = curso.alumnos.all().order_by('apellido', 'nombre')

    return render(request, 'asistencias/lista_observaciones.html', {
        'curso': curso,
        'alumnos': alumnos
    })

def consultas(request):
    return render(request, 'consultas/inicio.html')

def consultar_asistencias(request):

    asistencias = Asistencia.objects.none()

    curso_id = request.GET.get('curso')
    alumno_id = request.GET.get('alumno')

    if curso_id or alumno_id:

        asistencias = Asistencia.objects.all()

        if curso_id:
            asistencias = asistencias.filter(curso_id=curso_id)

        if alumno_id:
            asistencias = asistencias.filter(alumno_id=alumno_id)

        asistencias = asistencias.order_by('-fecha_hora')


    cursos = Curso.objects.all()
    alumnos = Alumno.objects.all()

    return render(request, 'consultas/consultar_asistencias.html', {
        'asistencias': asistencias,
        'cursos': cursos,
        'alumnos': alumnos
    })

def consultar_observaciones(request):

    observaciones = Observacion.objects.none()

    curso_id = request.GET.get('curso')
    alumno_id = request.GET.get('alumno')

    if curso_id or alumno_id:

        observaciones = Observacion.objects.all()

        if curso_id:
            observaciones = observaciones.filter(curso_id=curso_id)

        if alumno_id:
            observaciones = observaciones.filter(alumno_id=alumno_id)

        observaciones = observaciones.order_by('-fecha_hora')

    cursos = Curso.objects.all()
    alumnos = Alumno.objects.all()

    return render(request, 'consultas/consultar_observaciones.html', {
        'observaciones': observaciones,
        'cursos': cursos,
        'alumnos': alumnos
    })