
from django.urls import path
from .views import *

urlpatterns = [

    path('create', createCustomer),
    path('list', CustomerListView.as_view(),name="customer_list"),
]
