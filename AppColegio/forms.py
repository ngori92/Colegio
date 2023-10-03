from django import forms

class materiaFormulario(forms.Form):
    name = forms.CharField(max_length=30, required=False)
    grade = forms.IntegerField()