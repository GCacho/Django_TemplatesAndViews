#Python
from datetime import datetime
# Django
from django.shortcuts import render
from django.http import HttpResponse # Permite ejecutar respuesta HTTP
from django.template import Template, Context # Permite importar el contexto Context()
from django.template import loader # Permite trabajar con los cargadores de plantillas (templates) -> loader.get_template() desde settings.py

# Se puede trabajar con Programación Orientada a Objetos. (POO)
class Persona(object):

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

# Create your views here.
def index(request):                     # Este request viene el import HttpResponse
    p1 = Persona("guillermo", "CACHO")  # Se le da formato capitalize() en el template y si es 'guillermo' se mestra como profesor titular.
    ahora = datetime.now()
    listado = ["Plantillas","Modelos","Formularios", "Vistas", "Despliegue", "Testing"] # En caso de estar vacia la lista se hizo una restriccion con if en template 1 para evitar errores
    profesor = ["Titular", "Sustituto"]

    # ---------------------------Inicio Cargar Templates-----------------------------
    
    template_index = loader.get_template('index.html') # En la hoja de settings.py se asignan las plantillas con el loader
    
    ctx={  # Este es el contexto
            "nombre_persona": p1.nombre,
            "apellido_persona": p1.apellido, 
            "fecha_actual" : ahora,
            "temas": listado,
            "profesor": profesor
        }

    template = template_index.render(ctx) # El contexto son los datos que se migran al template para poder trabajar con ellos
    
    # ---------------------------Fin Cargar Templates-----------------------------
    
    return HttpResponse(template)      # Incrustamos la plantilla

    