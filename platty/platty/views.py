from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader

def index(request):
        return HttpResponse('Hey there, you are at the home index!')
# Create your views here.

def home(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

def create(request):
    return render_to_response('create.html', context_instance=RequestContext(request))

def parties(request):
    return render_to_response('parties.html', context_instance=RequestContext(request))

def find(request):
    return render_to_response('find.html', context_instance=RequestContext(request))

def login(request):
    return render_to_response('login.html', context_instance=RequestContext(request))

def profile(request):
    return render_to_response('profile.html', context_instance=RequestContext(request))
