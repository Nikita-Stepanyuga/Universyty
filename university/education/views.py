from django.shortcuts import render, redirect, get_object_or_404
from .forms import UniversityForm, StudentForm, TeacherForm, FacultyForm, DepartmentForm, GroupForm, DisciplineForm
from .models import University, Teacher, Student, Faculty, Department, Group, Discipline, Person

def create_university(request):
    if request.method == "POST":
        form = UniversityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("university_main.html")
    else:
        form = UniversityForm()

    return render(request, "education/university_form.html", {"form": form})

def university_list(request):
    universities = University.objects.all()
    return render(request, "education/university_main.html", {"universities": universities})

def university_detail(request, id):
    university = get_object_or_404(University, id=id)
    return render(request, 'education/university_detail.html', {'university': university})


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('university_main')
    else:
        form = StudentForm()
    return render(request, 'education/add_student.html', {'form': form})


def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name'].strip()
            last_name = form.cleaned_data['last_name'].strip()
            patronymic = form.cleaned_data['patronymic'].strip()

            person, created = Person.objects.get_or_create(
                name=first_name,
                surname=last_name,
                patronic=patronymic
            )

            teacher = form.save(commit=False)
            teacher.person = person
            teacher.save()

            form.save_m2m()

            return redirect('university_main')
    else:
        form = TeacherForm()

    return render(request, 'education/add_teacher.html', {'form': form})


def add_faculty(request):
    if request.method == 'POST':
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('university_main')
    else:
        form = FacultyForm()
    return render(request, 'education/add_faculty.html', {'form': form})

def faculty_list(request):
    faculties = Faculty.objects.all()
    return render(request, 'education/faculty_list.html', {'faculties': faculties})

def faculty_detail(request, id):
    faculty = get_object_or_404(Faculty, id=id)
    departments = faculty.department_set.all()
    return render(request, 'education/faculty_detail.html', {'faculty': faculty, 'departments': departments})

def faculty_edit(request, id):
    faculty = get_object_or_404(Faculty, id=id)
    if request.method == "POST":
        form = FacultyForm(request.POST, instance=faculty)
        if form.is_valid():
            form.save()
            return redirect('faculty_detail', id=faculty.id)
    else:
        form = FacultyForm(instance=faculty)

    return render(request, 'education/faculty_edit.html', {'form': form})

def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('university_main')
    else:
        form = DepartmentForm()

    return render(request, 'education/add_department.html', {'form': form})

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'education/department_list.html', {'departments': departments})

def department_detail(request, id):
    department = get_object_or_404(Department, id=id)
    faculty = department.faculty
    teachers = department.teachers.all()
    return render(request, 'education/department_detail.html', {
        'department': department,
        'faculty': faculty,
        'teachers':teachers
    })

def department_edit(request, id):
    department = get_object_or_404(Department, id=id)
    if request.method == "POST":
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_detail', id=department.id)
    else:
        form = DepartmentForm(instance=department)

    return render(request, 'education/department_edit.html', {'form': form})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'education/student_list.html', {'students': students})


def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('student_list')

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'education/teacher_list.html', {'teachers': teachers})

def delete_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    teacher.delete()
    return redirect('teacher_list')

def add_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('university_main')
    else:
        form = GroupForm()
        return render(request, 'education/add_group.html', {'form': form})

def group_list(request):
    groups = Group.objects.all()
    return render(request, 'education/group_list.html', {'groups': groups})

def group_detail(request, id):
    group = get_object_or_404(Group, id=id)
    students = Student.objects.filter(group=group)
    return render(request, 'education/group_detail.html', {'group': group, 'students': students})

def group_edit(request, id):
    group = get_object_or_404(Group, id=id)
    if request.method == "POST":
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('group_detail', id=group.id)
    else:
        form = GroupForm(instance=group)

    return render(request, 'education/group_edit.html', {'form': form})

def add_discipline(request):
    if request.method == 'POST':
        form = DisciplineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_discipline')
    else:
        form = DisciplineForm()

    return render(request, 'education/add_discipline.html', {'form': form})