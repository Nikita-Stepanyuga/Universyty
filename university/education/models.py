from django.db import models

class University(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, blank = True)

    def __str__(self):
        return self.name

class Discipline(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(
        'Department',
        on_delete=models.CASCADE,
        related_name='department_disciplines'
    )

    def __str__(self):
        return self.name

class Person (models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=50)
    patronic = models.CharField(max_length=50, blank = True)

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronic or ''}".strip()

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    faculty_head = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    head_teacher = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'teacher__isnull': False})

    def __str__(self):
        return self.name

class Teacher(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    Position = (
        ('Assistant', 'Асистент'),
        ('Lecturer','Преподаватель'),
        ('Seniot Lecturer','Старший преподователь'),
        ('Associate Professor','Доцент'),
        ('Professor','Профессор')
    )
    position = models.CharField(max_length=20, choices=Position, default='Assistant')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='teachers')
    disciplines = models.ManyToManyField(Discipline, through='Teaches', through_fields=('teacher', 'discipline'))

    def __str__(self):
        return f"{self.person}"

class Group(models.Model):
    name = models.CharField(max_length=20)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    curator = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.person} {self.status} {self.group}"

class Teaches(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('teacher', 'discipline')
