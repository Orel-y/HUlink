from django.urls import path
from .views import AnnouncementCreateListView, AnnouncementDetailView, CommentListCreateView

urlpatterns = [
    path('announcements/', AnnouncementCreateListView.as_view(), name='announcement-list'),
    path('announcements/<int:pk>', AnnouncementDetailView.as_view(), name='announcement-detail'),
    path('announcements/<int:announcement_id>/comments', CommentListCreateView.as_view(), name = 'comment-list')
]
