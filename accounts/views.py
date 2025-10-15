from django.core.serializers import serialize
from django.shortcuts import render
from accounts.serializers import  (UserSerializer, StudentSerializer,
                                   StaffSerializer, MentorSerializer,
                                   RegisterSerializer)
from accounts.models import  (CustomUser, Staff, Student, Mentor)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import  get_object_or_404

class RegisterAPIView(APIView):
    permission_classes =  [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.dat)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "messages": "user Registered Successfully",
                "user": UserSerializer(user).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentListAPIView(APIView):
    def get(self, request):
        all_student = Student.objects.all()
        serializer = StudentSerializer(all_student, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class StudentDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response({"error": "Student Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

class StaffListAPIView(APIView):
    def get(self, request):
        try:
            staff = Staff.objects.all()
        except:
            return Response({"error": "Something went down"}, status=status.HTTP_404_NOT_FOUND)

        serializer = StaffSerializer(staff, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MentorListAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        mentors = Mentor.objects.all()
        serializer = MentorSerializer(mentors, many=True)
        return Response(serializer.data)