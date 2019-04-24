from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .models import Student,Teacher
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.urls import reverse
import json
from django.http import JsonResponse
from django.core import serializers
# Create your views here.



def serve_data_view(request):
    if request.method=="GET":
        students = Student.objects.all()
        web_students = []
        os_students = []
        req_students = []
        business_students = []
        ethics_students = []
        net_students = []
        for student in students:
            if ' Web ' in student.subjects:
                web_students.append(student)
            elif ' Operating ' in student.subjects:
                os_students.append(student)
            elif ' Requirements ' in student.subjects:
                req_students.append(student)
            elif ' Business ' in student.subjects:
                business_students.append(student)
            elif ' Professional ' in student.subjects:
                ethics_students.append(student)
            elif 'Networking' in student.subjects:
                net_students.append(student)
        context={
        "os_students": len(os_students),
        "web_students" : len(web_students),
        "req_students" : len(req_students),
        "business_students" : len(business_students),
        "ethics_students" : len(ethics_students),
        "net_students" : len(net_students)
        }
        return JsonResponse(context)


def index(request):
    if request.user.is_authenticated:
        if request.method=="GET":
            context = {
            "user": request.user
            }
            return render(request,"index1.html",context)
    else:
        return HttpResponseRedirect(reverse("signup"))



def signup_view(request):
    if request.user.is_authenticated:
        return render(request,'index.html')
    else:
        if request.method == "POST":
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            username= request.POST["username"]
            password = request.POST["password"]
            email = request.POST["email"]
            user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password,email=email)
            user.save()
            return HttpResponseRedirect(reverse("signup"))
        else:
            return render(request,"signup.html")



def login_view(request):
    if request.user.is_authenticated:
        return render(request,'index.html')
    else:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return HttpResponseRedirect(reverse("signup"))

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render("error.html",{"message":" You are not logged in"})

def students_view(request):
    if request.user.is_authenticated:
        students = Student.objects.all()
        web_students = []
        os_students = []
        req_students = []
        business_students = []
        ethics_students = []
        net_students = []
        for student in students:
            if ' Web ' in student.subjects:
                web_students.append(student)
            elif ' Operating ' in student.subjects:
                os_students.append(student)
            elif ' Requirements ' in student.subjects:
                req_students.append(student)
            elif ' Business ' in student.subjects:
                business_students.append(student)
            elif ' Professional ' in student.subjects:
                ethics_students.append(student)
            elif 'Networking' in student.subjects:
                net_students.append(student)

        context = {
        "students": students,
        "os_students": os_students,
        "web_students" : web_students,
        "req_students" : req_students,
        "business_students" : business_students,
        "ethics_students" : ethics_students,
        "net_students" : net_students
        }
        return render(request,'students_html.html',context)
    else:
        return HttpResponseRedirect(reverse("signup"))

def student_detail_view(request,number):
    if request.user.is_authenticated:
        student = Student.objects.get(serial_no=number)
        context = {
        "student": student
        }
        return render(request,'student_detail.html',context)
    else:
        return HttpResponseRedirect(reverse("signup"))

def teachers_view(request):
    if request.user.is_authenticated:
        teachers = Teacher.objects.all()
        context = {
        "teachers": teachers
        }
        return render(request,"teachers_html.html",context)
    else:
        return HttpResponseRedirect(reverse("signup"))

def teacher_detail_view(request,id):
    if request.user.is_authenticated:
        teacher = Teacher.objects.get(id=id)
        context = {
        "teacher": teacher
        }
        return render(request,'teacher_detail.html',context)
    else:
        return HttpResponseRedirect(reverse("signup"))
