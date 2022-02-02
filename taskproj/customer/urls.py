from django.urls import path
from . import views
from .views import CustomerList

urlpatterns = [

    path('ls', CustomerList.as_view({'get': 'list'}))
]

