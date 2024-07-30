from django.contrib import admin
from .models import Group


class GroupSearch(admin.ModelAdmin):
    search_fields = ('group_type',)
    list_display = ['group_type', 'group_number', 'teacher', 'display_students']

    def save_model(self, request, obj, form, change):
        obj.name = obj.group_type
        obj.save()

    def display_students(self, obj):
        return ", ".join(student.name for student in obj.students.all())

    display_students.short_description = 'Students'

admin.site.register(Group, GroupSearch)
