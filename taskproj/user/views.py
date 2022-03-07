from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.views.generic import ListView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth import signals
from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from axes.decorators import axes_dispatch




def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'account/register.html', context)


class CustomLoginView(LoginView):
    template_name = 'account/login.html'


class ChangePasswordView(PasswordChangeView):
    template_name = 'account/changepass.html'
    success_url = reverse_lazy('home')

class ResetPassView(PasswordResetView):
    template_name = 'account/changepass.html'


class customerLogout(LogoutView):
    success_url = reverse_lazy('login')


@login_required
def Home(request):
    return render(request, 'account/Home.html')


class UserListView(ListView):
    context_object_name = 'ali_list'
    queryset = User.objects.all()
    template_name = 'account/userlist.html'


class AboutUs(TemplateView):
    template_name = 'account/aboutus.html'
    context_object_name = 'ali_list'
