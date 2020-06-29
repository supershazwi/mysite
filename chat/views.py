# chat/views.py
from django.http import HttpResponseRedirect
from django.shortcuts import render
from channels.layers import get_channel_layer

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

def test(request):
	return render(request, 'chat/test.html', {})