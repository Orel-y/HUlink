from django.urls import path
from .views import AnnouncementCreateListView, AnnouncementDetailView

urlpatterns = [
    path('announcements/', AnnouncementCreateListView.as_view(), name='announcement-list'),
    path('announcements/<int:pk>', AnnouncementDetailView.as_view(), name='announcement-detail')
]
