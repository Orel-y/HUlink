from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import AnnouncementListView, AnnouncementCreateView
from django.urls import reverse_lazy
urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', LoginView.as_view(template_name='announcement/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='announcement/logout.html'), name='logout'),
    path('register/', views.user_register_view, name='register'),
    path('profile/<int:pk>', views.profile_view, name='profile'),

    path('announcements/', AnnouncementListView.as_view(
        template_name='announcement/announcement_list.html'), 
        name='announcement_list'
    ),

    path('announcements/create/', AnnouncementCreateView.as_view(
        template_name='announcement/announcement_form.html'), 
        name='announcement_create'
    ),
]

