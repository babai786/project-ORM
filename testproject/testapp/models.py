from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=32)
    marks = models.IntegerField()
    dob = models.DateField()


    def __str__(self):
        return  self.name
