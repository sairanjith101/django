from django.shortcuts import render
from django.http import HttpResponse

def wish(request):
    message = '<h1>Hi buddy how are you</h1>'
    return HttpResponse(message)

# Create your views here.
