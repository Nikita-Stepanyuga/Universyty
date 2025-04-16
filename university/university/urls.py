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
from django.urls import path, include
from education import views

urlpatterns = [
    path('', views.university_list, name='university_main'),

    path('university/', include([
        path('<int:id>/', views.university_detail, name='university_detail'),
        path('create/', views.create_university, name='university_create_view'),
    ])),

    path('faculty/', include([
        path('', views.faculty_list, name='faculty_list'),
        path('<int:id>/', views.faculty_detail, name='faculty_detail'),
        path('<int:id>/edit/', views.faculty_edit, name='faculty_edit'),
    ])),

    path('department/', include([
        path('', views.department_list, name='department_list'),
        path('<int:id>/', views.department_detail, name='department_detail'),
        path('<int:id>/edit/', views.department_edit, name='department_edit'),
    ])),

    path('group/', include([
        path('', views.group_list, name='group_list'),
        path('<int:id>/', views.group_detail, name='group_detail'),
        path('<int:id>/edit/', views.group_edit, name='group_edit'),
    ])),

    path('student/', include([
        path('', views.student_list, name='student_list'),
        path('delete/<int:student_id>/', views.delete_student, name='delete_student'),
    ])),

    path('teacher/', include([
        path('', views.teacher_list, name='teacher_list'),
        path('delete/<int:teacher_id>/', views.delete_teacher, name='delete_teacher'),
    ])),

    path('add/', include([
        path('faculty/', views.add_faculty, name='add_faculty'),
        path('department/', views.add_department, name='add_department'),
        path('group/', views.add_group, name='add_group'),
        path('student/', views.add_student, name='add_student'),
        path('teacher/', views.add_teacher, name='add_teacher'),
        path('discipline/', views.add_discipline, name='add_discipline'),
    ])),

    path('admin/', admin.site.urls),
]