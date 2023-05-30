from django.db import models

# Create your models here.


class InnovateModel(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150,default="")
    department = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=300)
    benefits = models.CharField(max_length=300)
    plan = models.CharField(max_length=150)
    
