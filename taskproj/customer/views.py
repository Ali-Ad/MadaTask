from django.views.generic import ListView
from .models import Customer
from django.shortcuts import render, redirect
from .forms import InputForm
from django.contrib.auth.decorators import login_required

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
