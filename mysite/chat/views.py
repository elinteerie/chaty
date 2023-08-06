from django.shortcuts import render
from .models import Chatroom

def index(request):
    chatrooms = Chatroom.objects.all()
    
    return render(request, 'chat/index.html', {"chatroom": chatrooms})


def room(request, slug):
    room = Chatroom.objects.get(slug=slug)
    
    return render(request, 'chat/room.html', {"room": room})
    
    

    
    
