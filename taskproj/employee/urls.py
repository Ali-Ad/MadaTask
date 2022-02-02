from django.urls import path
from . import views
from .views import EmployeeView
urlpatterns = [
    path('add' , EmployeeView.as_view())
]
