from django.contrib import admin
from django.urls import path, include
from events.views import EventViewSet, ParticipantsViewSet
from rest_framework import routers

router= routers.DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'Participants', ParticipantsViewSet)

urlpatterns = [
    path('',include(router.urls))
   
]
