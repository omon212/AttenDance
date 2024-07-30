from django.contrib import admin
from .models import Teacher


class TeacherSearch(admin.ModelAdmin):
    search_fields = ('name',)

    def save_model(self, request, obj, form, change):
        obj.name = obj.name
        obj.save()


admin.site.register(Teacher, TeacherSearch, list_display=['name', 'email', 'phone'])
