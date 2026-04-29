from django.db import models
from django.contrib.auth.models import User

class Tarea(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('progreso', 'En progreso'),
        ('completado', 'Completado'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    creada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
