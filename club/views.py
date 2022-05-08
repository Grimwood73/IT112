from math import prod
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event

# Create your views here.
def index(request): 
    return render(request, 'club/index.html')

def resources(request):
    resource_list=Resource.objects.all()
    return render(request, 'club/resources.html', {'resource_list': resource_list})

def meetings(request):
    meetings_list=Meeting.objects.all()
    return render(request, 'club/meetings.html', {'meetings_list': meetings_list})

def meetingdetails(request, id):
    prod=get_object_or_404(Meeting, pk=id)
    context={
        'prod' : prod,
    }
    return render(request, 'club/meetingdetails.html', context=context)