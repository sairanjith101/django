from django.contrib import admin
from DBapp.models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    stu_details = ['studno', 'studname', 'studclass', 'studaddress']

admin.site.register(Student, StudentAdmin)
