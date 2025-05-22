from django.shortcuts import render
from .models import ParkingSpot

def available_spots_list(request):
    """
    View to list all parking spots that are currently available.
    """
    available_spots = ParkingSpot.objects.filter(is_available=True).order_by('spot_number')
    context = {
        'available_spots': available_spots,
        'page_title': 'Available Parking Spots'
    }
    return render(request, 'parking/available_spots_list.html', context)
