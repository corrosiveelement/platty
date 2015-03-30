from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader



def index(request):
        return HttpResponse('Hey there, you are at the signin index!')
# Create your views here.
