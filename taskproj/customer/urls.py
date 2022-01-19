from django.urls import path
from . import views
from .views import CustomerView

urlpatterns = [

    path('ls', CustomerView.as_view()),
    path('ls/<int:id>', CustomerView.as_view()),
]
