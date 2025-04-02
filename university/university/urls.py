"""
URL configuration for university project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from education import views

urlpatterns = [
    path('add_discipline/', views.add_discipline, name='add_discipline'),
    path('group/<int:id>/', views.group_detail, name='group_detail'),
    path('add_group/', views.add_group, name='add_group'),
    path('group/', views.group_list, name='group_list'),
    path('group/<int:id>/edit/', views.group_edit, name='group_edit'),
    path('students/', views.student_list, name='student_list'),
    path('delete/student/<int:student_id>/', views.delete_student, name='delete_student'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('university/<int:id>/', views.university_detail, name='university_detail'),
    path('', views.university_list, name='university_main'),
    path('university_create_view/', views.create_university, name='university_create_view'),
    path('add_student/', views.add_student, name='add_student'),
    path('add_teacher/', views.add_teacher, name='add_teacher'),
    path('delete/teacher/<int:teacher_id>/', views.delete_teacher, name='delete_teacher'),
    path('add_faculty/', views.add_faculty, name='add_faculty'),
    path('faculty/<int:id>/edit/', views.faculty_edit, name='faculty_edit'),
    path('faculties/', views.faculty_list, name='faculty_list'),
    path('faculty/<int:id>/', views.faculty_detail, name='faculty_detail'),
    path('add_department/', views.add_department, name='add_department'),
    path('departments/', views.department_list, name='department_list'),
    path('department/<int:id>/', views.department_detail, name='department_detail'),
    path('department/<int:id>/edit/', views.department_edit, name='department_edit'),
    path('admin/', admin.site.urls),
]
