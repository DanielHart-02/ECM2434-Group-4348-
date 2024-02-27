from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required
def view_recipe(request, recipe_id):
    return HttpResponse("Viewing recipe %d" % recipe_id)
