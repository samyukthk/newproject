from django.db import models

# Create your models here.


class School(models.Model):
    name=models.CharField( max_length=50)
    place=models.CharField( max_length=50)
    
    def __str__(self):
        return self.name



class Batch(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)
    name=models.CharField( max_length=50)
   
    def __str__(self):
        return self.name





class Student(models.Model):
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, null=True, blank=True)
    name=models.CharField( max_length=50)
    place=models.CharField( max_length=50)
    age=models.BigIntegerField()
    standard=models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.name