from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Room,Message
from django.http import HttpResponse, JsonResponse

def index(request):
    return render(request, 'chat/index.html')

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

def message(request):
    user=User.objects.all()
    return render(request,'chat/message.html',{'users':user})

def checkview(request,room_name):
    print(room_name)
    if Room.objects.filter(name=room_name).exists():
        print("room_detains id is ",room_name)
        return redirect('/chat/'+room_name)
    else:
        new_room = Room.objects.create(name=room_name)
        new_room.save()
        room_details = Room.objects.get(name=room_name)
        return render(request,'/chat/'+room_name,{'room_details':room_details})

def send(request):
    message = request.POST['message']
    room_name = request.POST['roomName']
    new_message = Message.objects.create(value=message,room=room_name)
    new_message.save()
    return HttpResponse('Message sent successfully')


def getMessages(request,room_name):
    messages = Message.objects.filter(room=room_name)
    return JsonResponse({"messages":list(messages.values())})
