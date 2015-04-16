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
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'selected_page': 'home'
    })
    return HttpResponse(template.render(context))


def create(request):
    template = loader.get_template('create.html')
    context = RequestContext(request, {
        'selected_page': 'create'
    })
    return HttpResponse(template.render(context))


def parties(request):
    event_list = Event.objects.filter().order_by('-id')[:5]
    template = loader.get_template('parties.html')
    context = RequestContext(request, {
        'event_list': event_list,
        'selected_page': 'parties'
    })
    return HttpResponse(template.render(context))

def party(request, id):
    event_list = Event.objects.filter(id=id)
    template = loader.get_template('create.html')
    context = RequestContext(request, {
        'event_list': event_list,
        'selected_page': 'create'
    })
    return HttpResponse(template.render(context))


def find(request):
    template = loader.get_template('find.html')

    searchedFor = request.GET.get('keywords', '')
    event_list = Event.objects.filter(name__icontains=searchedFor)

    context = RequestContext(request, {
        'event_list': event_list,
        'searched_for': searchedFor,
        'selected_page': 'find'
    })

    return HttpResponse(template.render(context))


def login(request):
    return render_to_response('login.html', context_instance=RequestContext(request))


def profile(request):
    template = loader.get_template('profile.html')
    context = RequestContext(request, {
        'selected_page': 'profile'
    })
    return HttpResponse(template.render(context))

def populate(request):
    event = Event(name="hey", zipCode=84321, description="A party", date_time=datetime.now())
    event.save()
    event = Event(name="A really cool party", zipCode=84321, description="The most best party ever always", date_time=datetime.now())
    event.save()

    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'selected_page': 'home'
    })
    return HttpResponse(template.render(context))
