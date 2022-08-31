from distutils.archive_util import make_archive
from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    pic = models.TextField(default='http://www.clipartbest.com/cliparts/LTK/Aa5/LTKAa55Ta.jpeg')
    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def isSexyAF(self):
        return True if self.first_name == 'Shannon' else False
        
class Car(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    make = models.CharField(max_length=255)


    def __str__(self):
        return (
            self.person.first_name + ' ' + self.person.last_name
             + ' that drives a ' + self.make.capitalize()
        )