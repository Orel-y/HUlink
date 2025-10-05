from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Announcement
from .forms import AnnouncementForm
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

def user_register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Has Registered")
            redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'announcement/register.html', {"form": form})

def home_view(request):
    return render(request, 'announcement/home.html')


@login_required
def profile_view(request, pk):
    user_profile = get_object_or_404(User, pk=pk)

    return render(request, 'announcement/profile.html', {"user_profile": user_profile})

#<li><a href="{%url 'announcements'%}">Announcements &#128226; </a></li>

class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'announcement/announcement_list.html'
    context_object_name = "announcements"
    ordering = ["-created_at"]

class AnnouncementCreateView(CreateView):
    model = Announcement
    template_name = 'announcement/announcement_form.html'
    form_class = AnnouncementForm
    success_url = reverse_lazy('announcement_list')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)