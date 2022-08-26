#Python
from datetime import datetime
# Django
from django.shortcuts import render
from django.http import HttpResponse #permite ejecutar respuesta HTTP
from django.template import Template, Context

class Persona(object):

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

# Create your views here.
def index(request): #Este request viene el import HttpResponse
    p1 = Persona("Guillermo", "Cacho")
    ahora = datetime.now()

    doc_externo=open("/home/cacho/pildoras-django/users/templates/template1.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx = Context({
        "nombre_persona":p1.nombre,
        "apellido_persona": p1.apellido,
        "fecha_actual" : ahora,
        "temas":["Plantillas","Modelos","Formularios", "Vistas", "Despliegue"]
        })
    documento = plt.render(ctx)
    return HttpResponse(documento) # Incrustamos la plantilla

    