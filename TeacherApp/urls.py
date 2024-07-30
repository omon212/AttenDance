from django.urls import path
from .views import *

urlpatterns = [
    path('teacher/teachers/', AllTeacherView.as_view(), name='All Teachers'),
    path('teacher/<int:id>/', TeacherDataView.as_view(), name='Teacher Data'),
    path('teacher/update/<int:id>/', TeacherUpdateView.as_view(), name='Teacher Update Data'),
    path('teacher/delete/<int:id>/', TeacherDeleteView.as_view(), name='Teacher Delete Data'),
]
