from django.views.generic import ListView
from .models import Customer
from django.shortcuts import render, redirect
from .forms import InputForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView

@login_required
def createCustomer(request):
    context = {}
    form = InputForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('customer_list')
    context['form'] = form
    return render(request, "index.html", context)


class CustomerListView(ListView):
    context_object_name = 'Customer_list'
    queryset = Customer.objects.all()
    template_name = 'help.html'

class DeleteView(DeleteView):
    model = Customer
    template_name = 'helped.html'
    success_url = "/customer/list"

class UpdateView(UpdateView):
    model=Customer
    fields=('__all__')
    template_name = 'helped1.html'
    success_url ="/customer/list"
