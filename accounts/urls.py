from django.urls import path
from .views import (
    RegisterAPIView,
    StudentListAPIView, StudentDetailAPIView,
    StaffListAPIView,
    MentorListAPIView
)

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),

    path('students/', StudentListAPIView.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentDetailAPIView.as_view(), name='student-detail'),

    path('staff/', StaffListAPIView.as_view(), name='staff-list'),

    path('mentors/', MentorListAPIView.as_view(), name='mentor-list'),
]
