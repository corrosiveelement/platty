from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader

def index(request):
        return HttpResponse('Hey there, you are at the home index!')
# Create your views here.

def home(request):
    return render_to_response('platty/index.html', context_instance=RequestContext(request))