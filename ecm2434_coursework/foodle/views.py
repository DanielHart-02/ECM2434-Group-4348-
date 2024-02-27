from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.models import UserProfile
from .models import MealEvents
from .forms import CreateMealEvent
from django.contrib.auth.decorators import login_required


def welcome(request):
    return render(request, "foodle/welcome.html")


@login_required
def home(request):
    return render(request, "foodle/home.html")


@login_required
def play(request):
    return HttpResponse("This is the Foodle game page")


@login_required
def events(request):
    user_group = request.user.groups.first()
    cooking_events = MealEvents.objects.filter(group=user_group)
    context = {"cooking_events": cooking_events}
    return render(request, "foodle/events.html", context)


@login_required
def create_event(request):
    if request.method == "POST":
        form = CreateMealEvent(request.POST)
        if form.is_valid():
            new_event = MealEvents(
                user=request.user,
                group=request.user.groups.first(),
                date_time=form.cleaned_data.get("date_time"),
                recipe=form.cleaned_data.get("recipe"),
            )
            new_event.save()
            return redirect('foodle:events')
            
    else:
        form = CreateMealEvent()
    return render(request, "foodle/create_event.html", {"form": form})


@login_required
def leaderboard(request):
    top_100_profiles = UserProfile.objects.order_by("foodle_score")[:100]
    context = {"top_100_profiles": top_100_profiles}
    return render(request, "foodle/leaderboard.html", context)
