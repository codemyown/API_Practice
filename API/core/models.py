from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length = 30)
    role = models.CharField(max_length = 30)
    salary = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.name
    
    
class City(models.Model):
    city = models.CharField(max_length  = 40)
    state = models.CharField(max_length = 30)
    name = models.ForeignKey(Student,on_delete = models.CASCADE)

    def __str__(self):
        return self.city