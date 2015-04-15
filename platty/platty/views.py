from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from .models import Event

def index(request):
        return HttpResponse('Hey there, you are at the home index!')
# Create your views here.

def home(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

def create(request):
 #   Event.objects.create(name= "Banana", location="The Congo", description="Why WOULDN'T you want a Congo banana
 #           party?",)
    event_list = Event.objects.order_by('-id')[:5]
    template = loader.get_template('create.html')
    context = RequestContext(request, {
        'event_list': event_list,
    })
    return HttpResponse(template.render(context))

def parties(request):
    return render_to_response('parties.html', context_instance=RequestContext(request))

def find(request):
    return render_to_response('find.html', context_instance=RequestContext(request))

def login(request):
    return render_to_response('login.html', context_instance=RequestContext(request))

def profile(request):
    return render_to_response('profile.html', context_instance=RequestContext(request))
