from django.urls import path
from .views import (
    RegisterAPIView, LoginAPIView, LogoutAPIView,
    StudentListAPIView, StudentDetailAPIView,
    StaffListAPIView,
    MentorListAPIView
)

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),

    path('students/', StudentListAPIView.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentDetailAPIView.as_view(), name='student-detail'),
    path('staff/', StaffListAPIView.as_view(), name='staff-list'),
    path('mentors/', MentorListAPIView.as_view(), name='mentor-list'),
]
