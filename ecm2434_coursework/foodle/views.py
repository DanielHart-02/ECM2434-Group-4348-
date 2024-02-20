from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "foodle/index.html")

def register(request):
    return HttpResponse("This is the registration page")

def play(request):
    return HttpResponse("This is the Foodle game page")

def user(request, user_id):
    return HttpResponse("This is user %d's page" % user_id)