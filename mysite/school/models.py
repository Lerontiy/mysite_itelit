from django.db import models

# Create your models here.

class Student(models.Model):
   name = models.CharField(max_length=20)
   lastname = models.CharField(max_length=20)
   post = models.TextField(max_length=50)

class Car(models.Model):
   number = models.IntegerField()
   name = models.CharField(max_length=20)

class Foto(models.Model):
   id_car = models.IntegerField()
   image = models.ImageField(upload_to='static/images' , height_field=None , width_field=None , max_length=None)