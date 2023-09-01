from django import forms

# Register your models here.

class EmployeeInfoForm(forms.Form):
    name = forms.CharField(max_length = 30)
    salary = forms.IntegerField()