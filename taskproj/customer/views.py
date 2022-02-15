from django.views.generic import ListView
from .models import Customer
from django.shortcuts import render
from .forms import InputForm


def createCustomer(request):
    context = {}
    form = InputForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "index.html", context)


class CustomerListView(ListView):
    context_object_name = 'Customer_list'
    queryset = Customer.objects.all()
    template_name = 'help.html'
