from django.shortcuts import render
from .models import Messages, Users


def index(request):
    room_names = Messages.objects.order_by('room_name').values('room_name').distinct()
    return render(request, "chat/index.html", {"room_names": room_names})


def room(request, room_name, username):
    messages = Messages.objects.filter(room_name=room_name)[0:25]
    return render(request, "chat/room.html", {"room_name": room_name, "username": username, "messages": messages})