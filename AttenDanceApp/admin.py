from django.contrib import admin
from .models import AttendanceModel

admin.site.register(AttendanceModel, list_display=('group', 'student', 'status', 'date'))
