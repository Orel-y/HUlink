from django.shortcuts import render
from .models import Announcement, User
from .serializers import AnnouncementSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class AnnouncementCreateListView(generics.ListCreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically assign the logged-in user as author
        serializer.save(author=self.request.user)


class AnnouncementDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)