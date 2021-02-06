from django.shortcuts import render, redirect
# vista basadas en funciones 
from .models import Persona
from .forms import PersonaForm
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    personas = Persona.objects.all() # orm
    contexto = {
        'personas': personas
    }
    return render(request, 'index.html', contexto )


def crearPersona(request):
    if request.method == 'GET':
        form = PersonaForm()
        contexto ={
            'form': form
            }
    else:
        form = PersonaForm(request.POST)
        print(form)
        # validando datos
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'crear_persona.html', {'form': form})

def editarPersona(request,id):
    persona = Persona.objects.get(id = id) # get nos permite resivir un valor
    if request.method =='GET':
        form = PersonaForm(instance= persona)
        contexto = {
            'form': form
        }
    else:
        form = PersonaForm(request.POST, instance = persona)
        contexto = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'crear_persona.html', contexto)

def eliminarPersona(request,id):
    persona = Persona.objects.get(id = id)
    persona.delete()
    return redirect('index')


    n1, n2, n3 = 5
    s = n1 + n2 + n3
    p = s /3
    return redirect('index')
