from django.shortcuts import render
from rest_framework import viewsets
from events.models import Event, Participants
from events.serializers import EventSerializer, ParticipantsSerializers
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.
class EventViewSet(viewsets.ModelViewSet):
    queryset= Event.objects.all()
    serializer_class=EventSerializer


    @action(detail=True, methods=['get'])
    def Participants(self,request,pk=None):
        try:
          Event=Event.objects.get(pk=pk)
          Participants=Participants.object.fliter(Event=Event)
          Participants_Serializers=ParticipantsSerializers(Participants,many=True,context={'request':request})
          return Response(Participants_Serializers.data)
        except Exception as e:
            print(e)
            return Response({
                    'message':'Event might not exist'
})

class ParticipantsViewSet(viewsets.ModelViewSet):
    queryset=Participants.objects.all()
    serializer_class=ParticipantsSerializers
