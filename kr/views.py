from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def kolkatta(request):
    return HttpResponse("Banglore is the capital of Kolkatta")

def hello(request):
    return render(request,'hello.html')