from django.urls import path
from . import views

urlpatterns= [
    path('',views.index,name="index"),
    path('students/',views.students_view,name="students"),
    path('students/<int:number>/',views.student_detail_view,name="student_detail"),
    path('teachers',views.teachers_view,name="teachers"),
    path('teachers/<int:id>/',views.teacher_detail_view,name="teacher_detail"),
    path('signup/',views.signup_view,name="signup"),
    path('login/',views.login_view,name="login"),
    path('logout/',views.logout_view,name="logout"),
    path('serve_data',views.serve_data_view,name="serve_data")
]
