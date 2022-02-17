from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Service
from django.shortcuts import render, redirect
from .forms import InputForm

@login_required
def create_view(request):
    context = {}
    form = InputForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('service_list')
    context['form'] = form
    return render(request, "index.html", context)


class ServiceListView(ListView):
    context_object_name = 'Service_list'
    queryset = Service.objects.all()
    template_name = 'hello.html'
