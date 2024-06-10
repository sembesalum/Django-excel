from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=150)
    second_name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    monthly_salary = models.CharField(max_length=10000)