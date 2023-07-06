from django.contrib import admin
from events.models import  Participants
# Register your models here.
class EventsAdmin(admin.ModelAdmin):
    list_display=('name','location','type')
admin.site.register('')
admin.site.register(Participants)


