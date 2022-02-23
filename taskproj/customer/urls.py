
from django.urls import path
from .views import *

urlpatterns = [

    path('create', createCustomer),
    path('list', CustomerListView.as_view(),name="customer_list"),
    path('<pk>/delete/', DeleteView.as_view(),name='delete'),
    path('<pk>/update/',UpdateView.as_view(), name ='update')

]
