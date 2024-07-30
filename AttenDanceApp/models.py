from django.db import models
from GroupApp.views import Group
from StudentApp.views import Student
from TeacherApp.views import Teacher


class AttendanceModel(models.Model):
    STATUS_CHOICES = [
        ('Keldi', 'Keldi'),
        ('Kelmadi', 'Kelmadi'),
        ('Kiritilmagan', 'Kiritilmagan'),
    ]
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Kiritilmagan')

    def __str__(self):
        return f'{self.student} - {self.status}'
