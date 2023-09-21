from django.contrib import admin
from crudApp.models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list = ['Sno', 'Sname', 'Sclass', 'Saddress']

admin.site.register(Student, StudentAdmin)