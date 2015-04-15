from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, loader

from django.db import models
from datetime import datetime
from .models import Event

def index(request):
        return HttpResponse('Hey there, you are at the home index!')
# Create your views here.

def home(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

def create(request):
    p = get_object_or_404(Event, pk=event_id)
    event = Event(date_time = datetime.now(), name="fdasfs", location="fdsfa", description="fdsafdsa")
    event_list = Event.objects.order_by('-id')[:5]
    template = loader.get_template('create.html')
    context = RequestContext(request, {
        'event_list': event_list,
    })
    #event.save()
    return HttpResponse(template.render(context))

def parties(request):
    return render_to_response('parties.html', context_instance=RequestContext(request))

def find(request):
    return render_to_response('find.html', context_instance=RequestContext(request))

def login(request):
    return render_to_response('login.html', context_instance=RequestContext(request))

def profile(request):
    return render_to_response('profile.html', context_instance=RequestContext(request))
