from django.shortcuts import render

def display(request):
    return render(request, 'templateapp/demo.html')
# Create your views here.
