from django.db import models
class Student (models.Model) :
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    GPA = models.FloatField(null=False,blank=False,default=0)
   
    email = models.EmailField()
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.name

    class Meta:
        db_table='student'

# Create your models here.
