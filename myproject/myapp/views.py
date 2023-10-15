from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import TemplateView

# Create your views here.

class FirstUserView(TemplateView):
    template_name = 'first_user.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        first_user = User.objects.first()
        context['first_user'] = first_user
        return context

class AllUsersView(TemplateView):
    template_name = 'all_users.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users = User.objects.all()
        context['users'] = users
        return context

class UserProfileView(TemplateView):
    template_name = 'user_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.kwargs.get('user_id')
        user = get_object_or_404(User, pk=user_id)
        context['user'] = user
        return context