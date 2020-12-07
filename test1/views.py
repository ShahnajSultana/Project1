from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("This is our First Project")



def contact(request):
    return HttpResponse("This is our contact page")

def service(request):
    return HttpResponse("This is our service page")

def info(request,name,age):
    return HttpResponse('{} is {} years old'.format(name,age))