from django.db import models

# Create your models here.

class Employement(models.Model):
    name = models.CharField(max_length=30,null=True,blank=True)
    title = models.CharField(max_length=30,null=True,blank=True)


    def __str__(self):
        return self.name

