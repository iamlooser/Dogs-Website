from django.shortcuts import render, HttpResponseRedirect
from event.models import Event
from upComingEvent.models import UpComingEvent
from django.db.models import Q
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    count=int(0)
    UpComingEventData = UpComingEvent.objects.all()
    EventData = Event.objects.all()
    date = datetime.date(datetime.now())
    size=len(EventData)
    return render(request, 'index.html',{'data_of_upComing_event':UpComingEventData,'data_of_event':EventData,'date':date,'count':count})

def search(request):

    UpComingEventData = UpComingEvent.objects.all()
    if request.method == 'POST':
        search = request.POST['search']

        if search:
            match = Event.objects.filter(Q(title__icontains=search) | Q(date__icontains=search) | Q(id__icontains=search))

            if match:
                return render(request, 'index.html', {'data_of_upComing_event':UpComingEventData,'data_of_event':match, 'search_item':search})
            else:
                msg_error = "no result found."
                return render(request, 'index.html', {'error_msg':msg_error})
        else:
            return HttpResponseRedirect('/')
    return render(request, 'index.html')

def sign_in(request):
    return render(request, 'signIn_page.html')

def signed_in(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            swal_msg = "swal"
            return render(request, 'signIn_page.html',{'swal_msg':swal_msg})
    else:
        return render(request, 'signIn_page.html')


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
