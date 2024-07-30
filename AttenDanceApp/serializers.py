from rest_framework import serializers
from .models import AttendanceModel


class AttenDanceAddSRL(serializers.ModelSerializer):
    class Meta:
        model = AttendanceModel
        fields = ('id', 'group', 'student', 'status', 'date')
