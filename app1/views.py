from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse("<h1>This is my first function of App1</h1>")

   