from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def second(request):
    return render(request,"htmlfile_1.html")


def hari(request):
    return render(request,"htmlfile_2.html")