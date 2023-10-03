from django.shortcuts import render
from django.http import HttpResponse
from AppColegio.models import *
from AppColegio.forms import * 

# Create your views here.
def inicio(request):
    return render(request, "AppColegio/index.html")
    
def cursos(request):
    return render(request, "AppColegio/materias.html")

def docentes(request):
    return render(request, "AppColegio/docentes.html")

def estudiantes(request):
    return render(request, "AppColegio/estudiantes.html")

def secundaria(request):
    return HttpResponse("Página de secundaria en construcción")

def inicial_primaria(request):
    return HttpResponse("Página de Inicial y Primaria en construcción")

def materia_formulario(request):
    
    if request.method == "POST":
        
        miFormulario = materiaFormulario(request.POST)
        
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
            
            materia = Materia(name=informacion["name"], grade=informacion["grade"])
            
            materia.save()
            
            return render(request, "AppColegio/index.html")
        
    else:
        
        miFormulario = materiaFormulario()
            
    return render(request, "AppColegio/materia-formulario.html", {"miFormulario": miFormulario})
        