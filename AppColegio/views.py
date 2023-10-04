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
        miFormulario = MateriaFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            materia = Materia(name=informacion["materia"], grade=informacion["grade"])
            materia.save()
            return render(request, "AppColegio/index.html")
        
    else:
        
        miFormulario = MateriaFormulario()
            
    return render(request, "AppColegio/materia-formulario.html", {"miFormulario": miFormulario})

def docente_formulario(request):
    if request.method == "POST":
        miFormulario = DocenteFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            docente = Docente(id_number=informacion["id_number"], first_name=informacion["first_name"], last_name=informacion["last_name"], entry_date=informacion["entry_date"])
            docente.save()
            return render(request, "AppColegio/index.html")
        
    else:
        
        miFormulario = DocenteFormulario()
            
    return render(request, "AppColegio/docente-formulario.html", {"miFormulario": miFormulario})

def estudiante_formulario(request):
    if request.method == "POST":
        miFormulario = EstudianteFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            estudiante = Estudiante(id_number=informacion["id_number"], first_name=informacion["first_name"], last_name=informacion["last_name"], birth_date=informacion["birth_date"], grade=informacion["grade"])
            estudiante.save()
            return render(request, "AppColegio/index.html")
        
    else:
        
        miFormulario = EstudianteFormulario()
            
    return render(request, "AppColegio/estudiante-formulario.html", {"miFormulario": miFormulario})

def busqueda_grade(request):
    
    return render(request, "AppColegio/busqueda-grade.html")

def buscar(request):
    
    if request.GET["grade"]:
        
        grade = request.GET["grade"]
        materias = Materia.objects.filter(grade__icontains=grade)
        
        return render(request, "AppColegio/resultados-busqueda.html", {"materias": materias, "grade":grade})
        
    else:
        respuesta = "No se enviaron datos" 
        
    return HttpResponse(respuesta)