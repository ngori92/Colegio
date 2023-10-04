from django import forms

class MateriaFormulario(forms.Form):
    materia = forms.CharField(max_length=30, required=False)
    grade = forms.IntegerField()
    
class DocenteFormulario(forms.Form):
    id_number = forms.IntegerField()
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    entry_date = forms.DateField()
    subject =  forms.CharField(max_length=30)
    
class EstudianteFormulario(forms.Form):
    id_number = forms.IntegerField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    birth_date = forms.DateField()
    grade = forms.IntegerField()