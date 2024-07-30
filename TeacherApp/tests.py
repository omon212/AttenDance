from django.test import TestCase
from .models import Teacher
from django.core.exceptions import ValidationError
from django.db import IntegrityError

try:
    teacher = Teacher.objects.create(name="John Doe", email="john@example.com", phone="123-456-7890")
    print(teacher.full_name)
except IntegrityError:
    print("A teacher with this email already exists.")
