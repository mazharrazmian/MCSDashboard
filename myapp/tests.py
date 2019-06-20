from django.test import TestCase

# Create your tests here.

from .models import Teacher,Student

class ModelsTestCase(TestCase):
    def setUp(self):

        t1 = Teacher.objects.create(id=20,first_name="Mazhar",last_name="Ali",email="abc@gmail.com",gender="male",subject="Web Development")
        t2 = Teacher.objects.create(id=30,first_name="Azhar",last_name="Ali",email="xyz@gmail.com",gender="male",subject="Web Development")

        Student.objects.create(serial_no=5,first_name="Areeba",last_name="majeed",subjects="Web Development",address="something",attendance=50)
        Student.objects.create(serial_no=7,first_name="Waqas",last_name="Ahmad",subjects="Web Development",address="something",attendance=50)


    def test_teacher_validation(self):
        t = Teacher.objects.get(id='20')
        print(t.id)
        self.assertTrue(t.is_valid(t.id,t.first_name))
