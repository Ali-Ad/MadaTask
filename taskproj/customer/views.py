from django.views.generic import ListView
from .models import Customer
from django.shortcuts import render, redirect
from .forms import InputForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView


def createCustomer(request):
    context = {}
    form = InputForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('customer_list')
    context['form'] = form
    return render(request, "index1.html", context)


class CustomerListView(ListView):
    model = Customer
    context_object_name = 'Customer_list'
    template_name = 'customerList.html'


class DeleteView(DeleteView):
    model = Customer
    template_name = 'deleteCustomer.html'
    success_url = "/customer/list"


class UpdateView(UpdateView):
    model = Customer
    fields = ('__all__')
    template_name = 'updateCustomer.html'
    success_url = "/customer/list"
