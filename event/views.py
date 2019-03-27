from django.shortcuts import render, HttpResponse
from event.models import Event, EventPhotos
from upComingEvent.models import UpComingEvent
from django.db.models import Q
from event.forms import EventForm


# Create your views here.
def event(request):
    EventData =  Event.objects.all()
    UpComingEventData = UpComingEvent.objects.all()
    return render(request, 'event/events.html',{ 'data_of_upComing_event':UpComingEventData,'data_of_event':EventData })

def event_details(request, event_id):
    UpComingEventData = UpComingEvent.objects.all()
    match = Event.objects.filter(Q(id__icontains=event_id))
    photos_id = match[0]
    EventPhtotoData = EventPhotos.objects.all()
    if match:
        return render(request, 'event/event_details.html', {'data_of_event':match, 'photo':EventPhtotoData, 'photo_id':photos_id})
    else:
        msg_error = "no result found."
        return render(request, 'event/event_details.html', {'data_of_upComing_event':UpComingEventData,'error_msg':msg_error})
