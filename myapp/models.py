from django.db import models

# Create your models here.



class Teacher(models.Model):
    id = models.IntegerField(primary_key=True,default=1)
    first_name = models.CharField(max_length=200,null=True)
    last_name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    gender = models.CharField(max_length=10,default="male")
    subject = models.CharField(max_length=50,null=True)

    def __str__(self):
        return f'{self.first_name}'

class Student(models.Model):
    serial_no = models.IntegerField(primary_key=True,default=1,max_length=100)
    first_name = models.CharField(max_length=40,null=True)
    last_name = models.CharField(max_length=40,null=True)
    subjects = models.CharField(max_length=500,null=True)
    address = models.CharField(max_length=50,null=True)
    attendance = models.FloatField(default=75)

    def __str__(self):
        return f'{self.first_name} is studying  {self.subjects}'
