from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    HttpResponse("this is the home page")


def room(request):
    HttpResponse("this is the room page")