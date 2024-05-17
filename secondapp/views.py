from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(rquest):
    return HttpResponse(f"<h1>Welcome to homeapp funtion</h1>")


def app_home(request):
    return HttpResponse(f',<h1>Welcome to second app home </h1>')


def work_fun(request):
    return HttpResponse(f'<h1>Welcome to work space</h1>')