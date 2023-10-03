from django.urls import path
from AppColegio.views import *

urlpatterns = [
    path('inicio/', inicio, name="Inicio"),
    path('materias/', cursos, name="Materias"),
    path('estudiantes/', estudiantes, name="Estudiantes"),
    path('docentes/', docentes, name="Docentes"),
    path('inicial-y-primaria/', inicial_primaria, name="Inicial y Primaria"),
    path('secundaria/', secundaria, name="Secundaria"),
    path('materia-formulario/', materia_formulario, name="Materia Formulario"),
]