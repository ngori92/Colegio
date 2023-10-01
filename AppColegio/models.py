from django.db import models

class Estudiante(models.Model):
    id_number = models.IntegerField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    grade = models.IntegerField()
    

class Docente(models.Model):
    id_number = models.IntegerField()    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    entry_date = models.DateField()
    
class Materia(models.Model):
    name = models.CharField(max_length=30)
    grade = models.IntegerField()
    