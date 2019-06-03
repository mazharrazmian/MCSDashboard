import csv

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mcs.settings")
import django
django.setup()
# your imports, e.g. Django models
from myapp.models import Student,Teacher

if len(Student.objects.all()) == 0:
    print("ZERO ZERO \n\n\n\n\n\n\n\nZERO ZERO\n\n\n")
    with open('students.csv') as f:
        print(Student.objects.all())
        reader = csv.reader(f,delimiter='|')
        for line in reader:
            try:
                q = Student.objects.get(serial_no=line[0])
            except Student.DoesNotExist:
                q = None
            if q is None:
                Student.objects.create(serial_no=line[0],first_name=line[1],last_name=line[2],subjects=line[3],address=line[4],attendance=line[5])



if len(Teacher.objects.all()) == 0:
    print(Teacher.objects.all())
    with open('teacher.csv') as f:
        reader = csv.reader(f,delimiter='|')
        for line in reader:
            try:
                q = Teacher.objects.get(id=line[0])
            except Teacher.DoesNotExist:
                q = None
            if q is None:
                Teacher.objects.create(id=line[0],first_name=line[1],last_name=line[2],email=line[3],gender=line[4],subject=line[5])
            


