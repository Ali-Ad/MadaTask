from django.urls import path
from .views import *

urlpatterns = [

    path('create', create_view),
    path('list', ServiceListView.as_view()),
]
