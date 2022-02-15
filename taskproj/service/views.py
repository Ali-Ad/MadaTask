from django.views.generic import ListView
from .models import Service
from django.shortcuts import render
from .forms import InputForm


def create_view(request):
    context = {}
    form = InputForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "index.html", context)


class ServiceListView(ListView):
    context_object_name = 'Service_list'
    queryset = Service.objects.all()
    template_name = 'hello.html'
