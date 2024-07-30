from rest_framework import serializers
from .models import Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class GroupStudentAddSRL(serializers.Serializer):
    student_id = serializers.IntegerField()
    group_id = serializers.IntegerField()