from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DeleteView, UpdateView, DetailView
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
    model = Service
    context_object_name = 'services'
    template_name = 'servicelist.html'


class ServiceDeleteView(DeleteView):
    model = Service
    template_name = 'deleteService.html'
    success_url = '/service/list'


class ServiceUpdateView(UpdateView):
    model = Service
    template_name = 'updateService.html'
    form_class = InputForm
    success_url = '/service/list'


class ServiceDetailView(DetailView):
    model = Service
    context_object_name = 'service'
    template_name = 'detailView.html'
