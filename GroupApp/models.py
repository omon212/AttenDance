from django.db import models
from StudentApp.models import Student
from TeacherApp.models import Teacher


class Group(models.Model):
    CHOICE = (
        ('BACK', 'BACK'),
        ('FRONT', 'FRONT'),
        ('FULLSTACK', 'FULLSTACK'),
        ('DEVOPS', 'DEVOPS'),
        ('STARTER', 'STARTER'),
    )
    group_type = models.CharField(choices=CHOICE, max_length=20)
    group_number = models.IntegerField(unique=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.group_type
