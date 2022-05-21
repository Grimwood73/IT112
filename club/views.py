from math import prod
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .forms import MeetingForm, ResourceForm
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

def newMeeting(request):
    form=MeetingForm

    if request.method=='POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingForm()
    else:
        form=MeetingForm()
    return render(request, 'club/newmeeting.html', {'form': form})

def newResource(request):
    form=ResourceForm

    if request.method=='POST':
        form=ResourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ResourceForm()
    else:
        form=ResourceForm()
    return render(request, 'club/newresource.html', {'form': form})