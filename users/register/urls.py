from django.urls import path
from . import views

urlpatterns = [ # Conexión con urls de la carpeta principal del proyecto.
    path('', views.index, name="index"), #Se recibe de views.py y se "carga" a urls.py de la carpeta del proyecto.
    path('cursopy/', views.cursopy, name="cursopy"),
    path('cursocss/', views.cursocss, name="cursocss"),
]