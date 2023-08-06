from django.shortcuts import render
from .models import Chatroom, ChatMessage

def index(request):
    chatrooms = Chatroom.objects.all()
    
    return render(request, 'chat/index.html', {"chatroom": chatrooms})


def room(request, slug):
    chatroom = Chatroom.objects.get(slug=slug)
    messages = ChatMessage.objects.filter(room=chatroom)
    
    return render(request, 'chat/room.html', {"room": chatroom,
                                              "messages": messages})
    
    

    
    
