from django.shortcuts import render
from formsApp import forms

# Create your views here.

def empDetailsView(request):
    form = forms.EmployeeInfoForm()
    empInfo = {'form' : form}
    return render(request, 'formsApp/input.html', context = empInfo)