from django.db import models

# Create your models here.



class Teacher(models.Model):
    id = models.CharField(primary_key=True,max_length=100)
    first_name = models.CharField(max_length=200,null=True)
    last_name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    gender = models.CharField(max_length=10,default="male")
    subject = models.CharField(max_length=50,null=True)

    def __str__(self):
        return f'{self.first_name}'
    
    def is_valid(self,id,name):
        print(id)
        available = Teacher.objects.filter(id=id)
        print(len(available))
        print(type(name))
        if len(available) is 1 and type(name) is str:
            return True
        else:
            return False


class Student(models.Model):
    serial_no = models.CharField(primary_key=True,max_length=100)
    first_name = models.CharField(max_length=40,null=True)
    last_name = models.CharField(max_length=40,null=True)
    subjects = models.CharField(max_length=500,null=True)
    address = models.CharField(max_length=50,null=True)
    attendance = models.FloatField(default=75)

    def __str__(self):
        return f'{self.first_name} is studying  {self.subjects}'
