from django.urls import path
from . import views
from .views import ServicesView
urlpatterns = [
    path('add' ,ServicesView.as_view ())
]
