from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    @property
    def full_name(self):
        return f"{self.name} {self.phone}"

