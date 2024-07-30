from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .models import *
from .serializers import *


class AllTeacherView(APIView):
    def get(self, request):
        try:
            teachers = Teacher.objects.all()
            serializer = TeacherSerializer(teachers, many=True)
            return Response(serializer.data, status=200)
        except Teacher.DoesNotExist:
            return Response({"error": "Teachers Not Found"}, status=404)


class TeacherDataView(APIView):
    def get(self, request, id):
        try:
            teacher = Teacher.objects.get(id=id)
            serializer = TeacherSerializer(teacher)
            return Response(serializer.data, status=200)
        except Teacher.DoesNotExist:
            return Response({"error": "Teacher Not Found"}, status=404)


class TeacherDeleteView(APIView):
    def delete(self, request, id):
        try:
            teacher = Teacher.objects.get(id=id)
            teacher.delete()
            return Response({"message": "Teacher Deleted"}, status=200)
        except Teacher.DoesNotExist:
            return Response({"error": "Teacher Not Found"}, status=404)


class TeacherUpdateView(APIView):
    @swagger_auto_schema(request_body=TeacherSerializer)
    def put(self, request, id):
        try:
            teacher = Teacher.objects.get(id=id)
        except Teacher.DoesNotExist:
            return Response({'error': 'Teacher not found'}, 404)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 200)
        else:
            return Response(serializer.errors, 400)
