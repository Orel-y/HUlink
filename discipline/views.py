# community/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .models import DisciplineReport
from .serializers import DisciplineReportSerializer
from accounts.models import Student, Staff

class DisciplineReportCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        student = request.user.student_profile
        serializer = DisciplineReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(student=student)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DisciplineReportListAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        if request.user.role != 'staff':
            return Response({"error": "Not authorized"}, status=status.HTTP_403_FORBIDDEN)
        reports = DisciplineReport.objects.all()
        serializer = DisciplineReportSerializer(reports, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DisciplineReportUpdateStatusAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, pk):
        if request.user.role != 'staff':
            return Response({"error": "Not authorized"}, status=status.HTTP_403_FORBIDDEN)
        report = DisciplineReport.objects.get(pk=pk)
        status_value = request.data.get('status')
        if status_value not in dict(DisciplineReport.STATUS_CHOICES):
            return Response({"error": "Invalid status"}, status=status.HTTP_400_BAD_REQUEST)
        report.status = status_value
        report.staff = request.user.staff_profile
        report.save()
        serializer = DisciplineReportSerializer(report)
        return Response(serializer.data, status=status.HTTP_200_OK)
