from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [

    path('create', createCustomer),
    path('list', login_required(CustomerListView.as_view()), name="customer_list"),
    path('<pk>/delete/', login_required(DeleteView.as_view()), name='delete'),
    path('<pk>/update/', login_required(UpdateView.as_view()), name='update')

]
