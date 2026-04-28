from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tareas, name='lista'),
    path('crear/', views.crear_tarea, name='crear'),
    path('completar/<int:id>/', views.completar_tarea, name='completar'),
    path('eliminar/<int:id>/', views.eliminar_tarea, name='eliminar'),
]