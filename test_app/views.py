from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse("Hi This is Home page")
def about(request):
    return HttpResponse("Hi This is About Page")
def contact(request):
    return HttpResponse("Hi This is Contact Page")

