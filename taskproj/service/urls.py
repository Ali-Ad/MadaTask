from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [

    path('create', create_view),
    path('list/', login_required(ServiceListView.as_view()), name="service_list"),
    path('<pk>/delete/', login_required(ServiceDeleteView.as_view()), name='deleteservice'),
    path('<pk>/update/', login_required(ServiceUpdateView.as_view()), name='updateservice'),
    path('<pk>/dd/',ServiceDetailView.as_view(),name='detailview')

]
