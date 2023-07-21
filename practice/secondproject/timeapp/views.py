from django.shortcuts import render
from django.http import HttpResponse
import datetime

def tellmetime(request):
    time = datetime.datetime.now()
    result = '<h1>Hi the time is : ' + str(time) + '</h1>'
    return HttpResponse(result)

    

# Create your views here.
