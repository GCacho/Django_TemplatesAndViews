#Python
from datetime import datetime
# Django
from django.shortcuts import render # Para migrar templates
# Se puede trabajar con Programación Orientada a Objetos. (POO)
class Persona(object):

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

# Create your views here.
def index(request):                     # Este request viene el import HttpResponse
    p1 = Persona("guillermo", "CACHO")  # Se le da formato capitalize() en el template y si es 'guillermo' se mestra como profesor titular.
    ahora = datetime.now()
    listado = ["Controlador","Plantillas","Modelos","Formularios", "Vistas", "Despliegue", "Testing"] # En caso de estar vacia la lista se hizo una restriccion con if en template 1 para evitar errores
    profesor = ["Titular", "Sustituto"]
    
    ctx={  # Este es el contexto
            "nombre_persona": p1.nombre,
            "apellido_persona": p1.apellido, 
            "fecha_actual" : ahora,
            "temas": listado,
            "profesor": profesor
        }
    
    return render(request, 'index.html', ctx) # Incrustamos la plantilla. En la hoja de settings.py se asignan las plantillas con el loader. Render es un shurtcut para migrar templates

def cursopy(request):
    fecha = datetime.now()
    return render(request, "cursopy.html", {"fecha": fecha})

def cursocss(request):
    fecha = datetime.now()
    return render(request, "cursocss.html", {"fecha": fecha})