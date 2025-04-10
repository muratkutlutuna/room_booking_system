from django.shortcuts import render
from .models import Room

def list_rooms(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms,
    }
    return render(request, 'rooms/list.html', context)
