from django.urls import URLPattern, path
from . import views

urlpatterns = [ # Conexión con urls de la carpeta principal del proyecto.
    path('', views.index, name="index"), #Se recibe de views.py y se "carga" a urls.py de la carpeta del proyecto.
    #ex: /polls/3/ --> permite acceder a la pregunta número 3
    path('<int:user_id>/', views.detail, name="index"), # '<int:user_id>/' es para pasar parametros a través de la url
]