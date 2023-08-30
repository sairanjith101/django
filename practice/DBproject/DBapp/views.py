from django.shortcuts import render
from DBapp.models import Student

# Create your views here.

def studDetails(request):
    #name = 'student'
    stud_data = Student.objects.all()
    stud_dict = {'stud_list' : stud_data}
    return render(request, 'DBapp/new.html', context = stud_dict)