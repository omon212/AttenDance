from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .models import *
from .serializers import *


class AllStudentView(APIView):
    def get(self, request):
        try:
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data, status=200)
        except Student.DoesNotExist:
            return Response({"error": "Students Not Found"}, status=404)


class StudentDataView(APIView):
    def get(self, request, id):
        try:
            students = Student.objects.get(id=id)
            serializer = StudentSerializer(students)
            return Response(serializer.data, status=200)
        except Student.DoesNotExist:
            return Response({"error": "Students Not Found"}, status=404)


class StudentDeleteView(APIView):
    def delete(self, request, id):
        try:
            student = Student.objects.get(id=id)
            student.delete()
            return Response({"message": "Student Deleted"}, status=200)
        except Student.DoesNotExist:
            return Response({"error": "Student Not Found"}, status=404)


class StudentUpdateView(APIView):
    @swagger_auto_schema(request_body=StudentSRL)
    def put(self, request, id):
        try:
            student = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({'error': 'Teacher not found'}, 404)
        serializer = StudentSRL(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 200)
        else:
            return Response(serializer.errors, 400)
