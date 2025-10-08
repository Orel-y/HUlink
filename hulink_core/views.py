from django.shortcuts import render, get_object_or_404
from .models import Announcement, User, Comment
from .serializers import AnnouncementSerializer, CommentSerializer
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
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        announcement_id = self.kwargs['announcement_id']
        return Comment.objects.filter(announcement_id=announcement_id)
    
    def perform_create(self, serializer):
        announcement_id = self.kwargs["announcement_id"]
        announcement = get_object_or_404(Announcement, id=announcement_id)
        serializer.save(author=self.request.user, announcement=announcement)