from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .models import *
from .serializers import *


class AttenDanceAdd(APIView):
    @swagger_auto_schema(request_body=AttenDanceAddSRL)
    def post(self, request):
        serializer = AttenDanceAddSRL(data=request.data)
        if serializer.is_valid():
            group_id = request.data['group']
            student_id = request.data['student']
            group = Group.objects.filter(id=group_id).first()
            if group:
                student_exists = group.students.filter(id=student_id).exists()
                if student_exists:
                    serializer.save()
                    return Response({'message': 'Attendance added'}, status=200)
                else:
                    return Response({'error': 'Student is not in this group'}, status=404)
            else:
                return Response({'error': 'Group not found'}, status=404)
        else:
            return Response({"error": "Invalid Data"}, status=400)


class AttenDanceAllData(APIView):

    def get(self, request, year, month):
        try:
            data = AttendanceModel.objects.filter(date__year=year, date__month=month)
            serializer = AttenDanceAddSRL(data, many=True)
            if not data.exists():
                return Response({'error': 'No data found'}, 404)
            updated_data = []
            for item in serializer.data:
                student_id = item['student']
                group_id = item['group']
                student = Student.objects.filter(id=student_id).first()
                group = Group.objects.filter(id=group_id).first()
                item['student'] = str(student)
                item['group'] = str(group)
                updated_data.append(item)
            return Response(updated_data, status=200)
        except AttendanceModel.DoesNotExist:
            return Response({'error': 'No data found'}, status=404)


class AttenDanceUpdate(APIView):
    def put(self, request, id):
        try:
            attendance = AttendanceModel.objects.get(id=id)
        except AttendanceModel.DoesNotExist:
            return Response({'error': 'Attendances not found'}, 404)
        serializer = AttenDanceAddSRL(attendance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 200)
        else:
            return Response(serializer.errors, 400)
