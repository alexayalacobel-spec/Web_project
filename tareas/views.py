from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea
from .forms import TareaForm
from django.contrib.auth.decorators import login_required

@login_required
def lista_tareas(request):
    tareas = Tarea.objects.filter(usuario=request.user)
    return render(request, 'tareas/lista.html', {'tareas': tareas})

@login_required
def crear_tarea(request):
    if request.method == 'POST':
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
    tarea = Tarea.objects.get(id=id)
    tarea.completada = True
    tarea.save()
    return redirect('lista')

@login_required
def eliminar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id, usuario=request.user)
    tarea.delete()
    return redirect('lista')