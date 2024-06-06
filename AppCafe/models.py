from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField(max_length=30)
    mesa=models.IntegerField()
    email=models.EmailField()

class Mesero(models.Model):
    nombre=models.CharField(max_length=30)
    mesa=models.IntegerField()

class Cuenta(models.Model):
    total=models.IntegerField()
    mesa=models.IntegerField()


