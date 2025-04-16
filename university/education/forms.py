from django import forms
from .models import University, Student, Teacher, Faculty, Department, Person, Group, Discipline, Teaches

class UniversityForm(forms.ModelForm):
    class Meta:
        model = University
        fields = ['name', 'phone_number']


class StudentForm(forms.ModelForm):
    first_name = forms.CharField(label="Имя", max_length=30)
    last_name = forms.CharField(label="Фамилия", max_length=50)
    patronymic = forms.CharField(label="Отчество", max_length=50, required=False)

    class Meta:
        model = Student
        fields = ['group', 'status']

    def save(self, commit=True):
        first_name = self.cleaned_data['first_name'].strip()
        last_name = self.cleaned_data['last_name'].strip()
        patronymic = self.cleaned_data['patronymic'].strip()


        person, created = Person.objects.get_or_create(
            name=first_name,
            surname=last_name,
            patronic=patronymic
        )

        student = super().save(commit=False)
        student.person = person
        if commit:
            student.save()

        return student

class TeacherForm(forms.ModelForm):
    first_name = forms.CharField(label="Имя", max_length=30)
    last_name = forms.CharField(label="Фамилия", max_length=50)
    patronymic = forms.CharField(label="Отчество", max_length=50, required=False)
    disciplines = forms.ModelMultipleChoiceField(
        queryset=Discipline.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control selectpicker', 'data-live-search': 'true'}),
        required=False,
        label="Выберите дисциплины"
    )
    class Meta:
        model = Teacher
        fields = ['position', 'department','disciplines']

    def save(self, commit=True):
        first_name = self.cleaned_data['first_name'].strip()
        last_name = self.cleaned_data['last_name'].strip()
        patronymic = self.cleaned_data['patronymic'].strip()

        person, created = Person.objects.get_or_create(
            name=first_name,
            surname=last_name,
            patronic=patronymic
        )

        teacher = super().save(commit=False)
        teacher.person = person
        if commit:
            teacher.save()

            Teaches.objects.filter(teacher=teacher).delete()

            for discipline in self.cleaned_data['disciplines']:
                Teaches.objects.create(teacher=teacher, discipline=discipline)

        return teacher

class DisciplineForm(forms.ModelForm):
    class Meta:
        model = Discipline
        fields = ['name', 'department']

class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['name', 'faculty_head', 'university']

class DepartmentForm(forms.ModelForm):
    disciplines = forms.ModelMultipleChoiceField(
        queryset=Discipline.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Department
        fields = ['faculty', 'name', 'head_teacher', 'disciplines']

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'faculty', 'curator']

