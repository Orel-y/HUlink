from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework.status import HTTP_200_OK, HTTP_205_RESET_CONTENT, HTTP_400_BAD_REQUEST
from accounts.models import  (CustomUser, Staff, Student, Mentor)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import  get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from accounts.serializers import  (UserSerializer, StudentSerializer,
                                   StaffSerializer, MentorSerializer,
                                   RegisterSerializer)


class RegisterAPIView(APIView):
    permission_classes =  [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "messages": "user Registered Successfully",
                "user": UserSerializer(user).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data
            })
        return Response({"error": "invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logout Successfully"},

                            status=HTTP_205_RESET_CONTENT)
        except Exception:
            return Response({"error": "Invalid Token"}, status=HTTP_400_BAD_REQUEST)

class StudentListAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class StudentDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def delete(self, request, pk):
        if request.user.role not in ['staff', 'admin']:
            return Response({"error": "Not authorized"}, status=status.HTTP_403_FORBIDDEN)

        student = get_object_or_404(Student, user__id=pk)
        student.delete()
        return Response({"sucess": "Student deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class ProfileView(APIView):
    def get(self, request):
        user = request.user
        return Response({"user-info": UserSerializer(user).data},
                            status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            student = serializer.save(user=request.user)
            return Response({
                "success": "Student Created Successfully",
                "student": StudentSerializer(student).data
            },
                status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StaffListAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        staff = Staff.objects.all()
        serializer = StaffSerializer(staff, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class StaffDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        staff = get_object_or_404(Staff, pk=pk)
        serializer = StaffSerializer(staff)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        if request.user.role not in ['staff', 'admin']:
            return Response({"error": "Not authorized"}, status=status.HTTP_403_FORBIDDEN)

        staff = get_object_or_404(Staff, user__id=pk)
        staff.delete()
        return Response({"message": "Staff deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class MentorListAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        mentors = Mentor.objects.all()
        serializer = MentorSerializer(mentors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)