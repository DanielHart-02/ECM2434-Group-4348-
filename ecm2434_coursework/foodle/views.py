from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "foodle/home.html")

def play(request):
    return HttpResponse("This is the Foodle game page")