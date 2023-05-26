from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def msd(request):
    return HttpResponse('<h1>Dhoni is CSK Player</h1>')

def hi(request):
    return render(request,'hi.html')