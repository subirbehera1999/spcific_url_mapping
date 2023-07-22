from django.shortcuts import render
 
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse("first function of app1")
def second(request):
    return HttpResponse("second function of app1")