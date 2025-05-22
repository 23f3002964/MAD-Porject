from django.urls import path
from . import views

app_name = 'parking'  # Namespace for the parking app URLs

urlpatterns = [
    path('available-spots/', views.available_spots_list, name='available_spots_list'),
]
