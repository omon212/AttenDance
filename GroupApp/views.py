from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .models import *
from .serializers import *
from StudentApp.models import Student


class AllGroupView(APIView):
    def get(self, request):
        try:
            groups = Group.objects.all()
            serializer = GroupSerializer(groups, many=True)
            data = serializer.data
            for group in data:
                student_names = Student.objects.filter(id__in=group['students']).values_list('name', flat=True)
                group['students'] = list(student_names)
                group['teacher'] = Teacher.objects.get(id=group['teacher']).name
            return Response(data, status=200)
        except Group.DoesNotExist:
            return Response({'error': 'Group Not Found'}, status=400)


class GroupView(APIView):
    def get(self, request, id):
        try:
            group = Group.objects.get(id=id)
            serializer = GroupSerializer(group)
            data = serializer.data
            student_names = Student.objects.filter(id__in=data['students']).values_list('name', flat=True)
            data['students'] = list(student_names)
            data['teacher'] = Teacher.objects.get(id=data['teacher']).name
            return Response(data, status=200)
        except Group.DoesNotExist:
            return Response({'error': 'Group Not Found'}, status=400)


class GroupDeleteView(APIView):
    def delete(self, request, id):
        try:
            group = Group.objects.get(id=id)
            group.delete()
            return Response({'message': 'Group Deleted'}, status=200)
        except Group.DoesNotExist:
            return Response({'error': 'Group Not Found'}, status=400)


class GroupUpdateView(APIView):
    @swagger_auto_schema(request_body=GroupSerializer)
    def put(self, request, id):
        try:
            group = Group.objects.get(id=id)
            serializer = GroupSerializer(group, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Group Updated'}, status=200)
            return Response(serializer.errors, status=400)
        except Group.DoesNotExist:
            return Response({'error': 'Group Not Found'}, status=400)


# class GroupStudentAdd(APIView):
#
#     @swagger_auto_schema(request_body=GroupStudentAddSRL)
#     def post(self, request):
#         try:
#             serializer = GroupStudentAddSRL(data=request.data)
#             if serializer.is_valid():
#                 student = Student.objects.get(id=serializer.validated_data['student_id'])
#                 if student:
#                     group = Group.objects.get(id=serializer.validated_data['group_id'])
#                     if group:
#                         group.students.add(student)
#                         return Response({'message': 'Student Added to Group'}, status=200)
#                     else:
#                         return Response({'error': 'Group Not Found'}, status=400)
#                 else:
#                     return Response({'error': 'Student Not Found'}, status=400)
#             else:
#                 return Response({'error': 'Invalid Data'}, status=400)
#         except Exception as e:
#             return Response({'error': "Invalid Data"}, status=500)
#
#
# class GroupStudentRemove(APIView):
#
#     @swagger_auto_schema(request_body=GroupStudentAddSRL)
#     def delete(self, request):
#         try:
#             serializer = GroupStudentAddSRL(data=request.data)
#             if serializer.is_valid():
#                 student = Student.objects.get(id=serializer.validated_data['student_id'])
#                 if student:
#                     group = Group.objects.get(id=serializer.validated_data['group_id'])
#                     if group:
#                         group.students.remove(student)
#                         return Response({'message': 'Student Removed from Group'}, status=200)
#                     else:
#                         return Response({'error': 'Group Not Found'}, status=400)
#                 else:
#                     return Response({'error': 'Student Not Found'}, status=400)
#             else:
#                 return Response({'error': 'Invalid Data'}, status=400)
#         except Exception as e:
#             return Response({'error': 'Invalid Data'}, status=500)
