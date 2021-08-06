from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('message/',message,name='message'),
    path('send/',send, name='send'),
    path('getMessages/<str:room_name>',getMessages, name='getMessages'),
    path('checkview/<str:room_name>/',checkview, name='checkview'),
    path('<str:room_name>/',room, name='room'),
]