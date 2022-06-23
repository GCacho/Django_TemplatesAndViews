# Python
import datetime
# Django
from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    email = models.EmailField(max_length=100)

    def __str__(self): #Método dunder string
        return self.question_text #Que muestre el valor del texto

    def was_published_recently(self):
        return self.pub_date >= timezone.timezone.now() - datetime.timedelta(days=1)