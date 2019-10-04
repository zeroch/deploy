from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=255)
    balance = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class Patient(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)