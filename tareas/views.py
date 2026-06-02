from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea
from .forms import TareaForm
from django.contrib.auth.decorators import login_required

@login_required
def lista_tareas(request):
    pendientes = Tarea.objects.filter(usuario=request.user, estado='pendiente')
    progreso = Tarea.objects.filter(usuario=request.user, estado='progreso')
    completadas = Tarea.objects.filter(usuario=request.user, estado='completado')
    
    return render(request, 'tareas/lista.html', {
        'pendientes': pendientes,
        'progreso': progreso,
        'completadas': completadas,
    })

@login_required
def crear_tarea(request):
    form = TareaForm(request.POST)
    if form.is_valid():
        tarea = form.save(commit=False)
        tarea.usuario = request.user
        tarea.save()
        
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')

        Tarea.objects.create(
            usuario=request.user,
            titulo=titulo,
            descripcion=descripcion
        )
        return redirect('lista')

    return render(request, 'tareas/crear.html')

@login_required
def completar_tarea(request, id):
    tarea = get_object_or_404(Tarea,id=id,usuario=request.user)
    tarea.estado = 'completado'
    tarea.save()
    return redirect('lista')

@login_required
def eliminar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id, usuario=request.user)
    tarea.delete()
    return redirect('lista')

@login_required
def cambiar_estado(request, id, estado):
    tarea = get_object_or_404(Tarea, id=id, usuario=request.user)
    tarea.estado = estado
    tarea.save()
    return redirect('lista')
