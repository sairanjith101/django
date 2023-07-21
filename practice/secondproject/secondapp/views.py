from django.shortcuts import render
from django.http import HttpResponse

def gm(request):
    return HttpResponse('<h1>Good Morning</h1>')

def gf(request):
    return HttpResponse('<h1>Good Afternoon</h1>')

def ge(request):
    return HttpResponse('<h1>Good Evening</h1>')

# Create your views here.
