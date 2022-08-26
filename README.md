# Django_practice
## Practice proyects with Django, Python and PostgreSQL
-----
### Basic Installations and Upgrades (pip and venv)
- sudo apt-get update
- sudo apt-get install python3-pip
- python3 -m pip install --upgrade pip
- sudo apt-get install python3-venv
- python3 -m venv venv
### Run Virtual Enviroment and Django
- source venv/bin/activate
- pip install -r requirements.txt 
- django-admin startproject users (Solo si no existen previamente)
- python3 manage.py startapp register (Solo si no existen previamente)
- python3 manage.py migrate
### Run Server
- python3 manage.py runserver
---------
### Crear Archivos Extra 
- Crear Archivo -> views.py
- Crear Carpeta -> templates
### Exportar modelos
- python3 manage.py makemigrations register
- python3 manage.py migrate
### Crear SuperUsuario
- python3 manage.py createsuperuser
