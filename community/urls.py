from django.urls import path
from .views import PetitionListCreateView, AnnouncementListCreateView, CommentListCreateView

urlpatterns = [
    path('petitions/', PetitionListCreateView.as_view(), name='petition-list-create'),
    path('announcements/', AnnouncementListCreateView.as_view(), name='announcement-list-create'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
]