from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse("first funtion of app2")
def second(request):
    return HttpResponse("second function of app2")