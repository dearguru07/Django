from django.shortcuts import render
from django.http import HttpResponse


def homePage(request):
    x='this is first view'
    return HttpResponse(x)
def conatct(request):
    x='this is second view'
    return HttpResponse(x)
def about(request):
    x='this is third view'
    return HttpResponse(x)
def bodyPage(request):
    y='this is forth view'
    return HttpResponse(y)