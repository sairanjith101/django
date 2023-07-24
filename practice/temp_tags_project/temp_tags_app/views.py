from django.shortcuts import render
import datetime

# Create your views here.

def display(request):
    date = datetime.datetime.now()
    dict_date = {'display_date':date}
    return render(request, 'temp_tags_app/input.html', context = dict_date)