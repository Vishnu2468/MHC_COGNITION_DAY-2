from django.contrib import admin

# Register your models here.

from .models import Student
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name','email','grade','address')