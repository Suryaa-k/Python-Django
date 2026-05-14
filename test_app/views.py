from django.http import HttpResponse
from django.shortcuts import render
from .models import Student

def index(request):
    std=Student.objects.all()
    return render(request,'index.html',{'students':std})

def get_student(request,pk):
    std=Student.objects.get(id=pk)
    return render(request,'index.html',{'students':std})




