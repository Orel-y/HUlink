from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', LoginView.as_view(template_name='announcement/login.html'), name='login'),
    path('login/', LogoutView.as_view(template_name='announcement/logout.html'), name='logout'),
    path('register/', views.user_register_view, name='register'),
    path('profile/<int:pk>', views.profile_view, name='profile')
]
