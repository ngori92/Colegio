from django.urls import path
from AppColegio.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('inicial-y-primaria/', inicial_primaria, name="Inicial y Primaria"),
    path('secundaria/', secundaria, name="Secundaria"),
    path('materia-formulario/', materia_formulario, name="Materia Formulario"),
    path('docente-formulario/', docente_formulario, name="Docente Formulario"),
    path('estudiante-formulario/', estudiante_formulario, name="Estudiante Formulario"),
    path('busqueda-grade/', busqueda_grade, name="Busqueda Grado"),
    path('buscar/', buscar, name="Buscar"),
]