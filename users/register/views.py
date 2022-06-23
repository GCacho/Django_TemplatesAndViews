#Python
from datetime import datetime
# Django
from django.shortcuts import render
from django.http import HttpResponse #permite ejecutar respuesta HTTP

# Create your views here.
def index(request): #Este request viene el import HttpResponse
    date = datetime.now()
    return HttpResponse(f"Registro de Usuarios {date.date()}") #Se manda a urls.py 

def detail(request, user_id):
    return HttpResponse(f"Estás viendo al usuario número: {user_id}")