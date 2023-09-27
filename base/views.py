from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room, Topic
from .forms import RoomForm
# Create your views here.
member_vehicles = [
  {
    
    "name": "Sara Silver",
    "vehicle_type": "Mazda Alexa",
    "vehicle_plate": "KAE892"
  },
  {
    "name": "Paul M",
    "vehicle_type": "Land Rover T110",
    "vehicle_color": "All Black",
    "vehicle_plate": "18CCM"
  },
  {
    "name": "Sandra Bullock",
    "vehicle_type": "Mobius",
    "vehicle_plate": "KEKMM123X"
  },
  {
    "name": "Natalie A",
    "vehicle_type": "Range Rover T110",
    "vehicle_plate": "L0ZIKRE"
  }
]

def home(request):
    rooms = Room.objects.all() # model manager

    topics = Topic.objects.all()

    context = {
        'name_rooms': rooms,
        'name_topics': topics,
        }
    return render(request, 'base/home.html', context) # Render request is how we pass data back and forth
    # return HttpResponse('Home Page') : Replace method

def room(request, pk):
    # room = None 
    # for i in rooms:
    #     if i['name'] == str(pk):
    #         room = i
    room = Room.objects.get(id=pk)
    
    context = {'room': room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})