from django.shortcuts import render
# from django.http import HttpResponse
# # Create your views here.
# def hello_world(request):
#     return HttpResponse("Hello, World!")
# def home(request):
#     return HttpResponse("This is Home page")
# def about(request):
#     return HttpResponse("This is about page")
# def contact(request):
#     return HttpResponse("This is Contact page")
# def profile(request):
#     return HttpResponse("This is profile page")
# def tvishnu(request):
#     return render(request,'vishnu.html')

from django.shortcuts import render
from .models import Student
def vishnu(request):
    #Query all students records
    students=Student.objects.all()
    #Render the list template with the student data
    return render(request,'vishnu.html',{'std':students})