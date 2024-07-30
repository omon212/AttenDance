from django.urls import path
from .views import *

urlpatterns = [
    path('student/students/', AllStudentView.as_view(), name='All Students'),
    path('student/<int:id>/', StudentDataView.as_view(), name='Student Data'),
    path('student/update/<int:id>/', StudentUpdateView.as_view(), name='Student Update Data'),
    path('student/delete/<int:id>/', StudentDeleteView.as_view(), name='Student Delete'),
]
