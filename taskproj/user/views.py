from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.views.generic import ListView


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'account/register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    context = {}
    return render(request, 'account/login.html', context)

def logoutuser(request):
    logout(request)
    return redirect('login')
def Home(request):
    return render(request,'account/Home.html')


class UserListView(ListView):
    context_object_name = 'ali_list'
    queryset = User.objects.all()
    template_name = 'account/hello.html'
