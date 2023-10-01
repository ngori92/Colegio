from django.shortcuts import render
# from django.template import Template, Context
# from django.template import loader
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, "AppColegio/index.html")
    
def cursos(request):
    return render(request, "AppColegio/materias.html")

def docentes(request):
    return render(request, "AppColegio/docentes.html")

def estudiantes(request):
    return render(request, "AppColegio/estudiantes.html")