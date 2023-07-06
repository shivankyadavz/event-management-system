from rest_framework import serializers
from events.models import Event, Participants

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class ParticipantsSerializers(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()

    class Meta:
        model=Participants
        fields="__all__"