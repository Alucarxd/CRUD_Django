from django.db import models

# Create your models here.

class Persona(models.Model):
    id = models.AutoField(primary_key= True) # espeficinando que es la clave primaria y es autoincrementable
    nombre = models.CharField(max_length= 100) # , unique= True para no repetir el mismo valor, tipo char maximo caracter 100
    apellido = models.CharField(max_length= 120)
    correo = models.EmailField(max_length= 200) # tipo correo 

    # mostras nombre diferente
    def __str__(self):
        return self.nombre