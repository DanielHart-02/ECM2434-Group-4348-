# views.py
from django.shortcuts import redirect

def redirect_home(request):
    response = redirect('/foodle/home/')
    return response