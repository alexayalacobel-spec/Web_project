from django.shortcuts import render, redirect
from .models import Tarea
from .forms import TareaForm

def lista_tareas(request):
    tareas = Tarea.objects.order_by('-creada')
    return render(request, 'lista.html', {'tareas': tareas})

def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = TareaForm()

    return render(request, 'tareas/crear.html', {'form': form})

def completar_tarea(request, id):
    tarea = Tarea.objects.get(id=id)
    tarea.completada = True
    tarea.save()
    return redirect('lista')

def eliminar_tarea(request, id):
    tarea = Tarea.objects.get(id=id)
    tarea.delete()
    return redirect('lista')